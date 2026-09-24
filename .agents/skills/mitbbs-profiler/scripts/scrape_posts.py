#!/usr/bin/env python3
"""
MITBBS Full User Post Scraper & Separator
Supports:
1. Direct Usernames (e.g. "foxbat", "牛河梁", "coolcat")
2. Direct Author IDs (e.g. "3858", "16040")
3. Full URLs (e.g. search.php?author_id=... or search.php?author=...)
Handles full pagination (--all), phpBB flood control, and quote/reply separation.
"""

import sys
import os
import re
import ssl
import json
import time
import html
import urllib.request
import urllib.parse
from collections import Counter

# Set up SSL context (bypasses cert verify errors on local macOS system pythons)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

def clean_html_text(s):
    """Clean HTML tags and unescape entities."""
    s = re.sub(r'<[^>]+>', ' ', s)
    return " ".join(html.unescape(s).split())

def resolve_target(input_str):
    """
    Resolves input_str (which can be a URL, numeric author_id, or username)
    into a tuple of (author_id, username).
    """
    input_str = input_str.strip()
    
    # Case 1: Pure numeric author_id
    if input_str.isdigit():
        return input_str, None
        
    # Case 2: URL with author_id or u parameter
    if "newmitbbs.com" in input_str or "http" in input_str:
        m_id = re.search(r'[?&](?:author_id|u)=(\d+)', input_str)
        if m_id:
            return m_id.group(1), None
            
        m_auth = re.search(r'[?&]author=([^&]+)', input_str)
        if m_auth:
            input_str = urllib.parse.unquote(m_auth.group(1))
            
    KNOWN_ALIASES = {
        "蒙古大夫": "lexian",
    }
    if input_str in KNOWN_ALIASES:
        username = KNOWN_ALIASES[input_str]
        print(f"[*] Mapped alias '{input_str}' -> '{username}'")
    else:
        username = input_str

    print(f"[*] Resolving username '{username}' to author_id on NewMitBBS...")
    encoded_user = urllib.parse.quote(username)
    url = f"https://newmitbbs.com/search.php?author={encoded_user}&sr=posts"
    req = urllib.request.Request(url, headers=HEADERS)
    
    try:
        resp = urllib.request.urlopen(req, context=ctx, timeout=15).read().decode("utf-8", errors="replace")
        
        # Check flood protection
        if "对不起您现在不能使用搜索" in resp:
            time.sleep(2)
            resp = urllib.request.urlopen(req, context=ctx, timeout=15).read().decode("utf-8", errors="replace")
            
        # Extract author_id from search results
        m_id = re.search(r'author_id=(\d+)', resp)
        if m_id:
            resolved_id = m_id.group(1)
            print(f"[+] Successfully resolved '{username}' -> author_id: {resolved_id}")
            return resolved_id, username
            
        # Check if user not found
        if "找不到与指定条件相符的结果" in resp or "指定的用户名不存在" in resp:
            raise ValueError(f"User '{username}' was not found on NewMitBBS.")
            
    except Exception as e:
        print(f"[!] Warning during username resolution: {e}")
        
    raise ValueError(f"Could not resolve target author for input: '{input_str}'")

def parse_post_content(raw_content_html):
    """
    Separates the quoted original text being replied to from the user's own reply text.
    Returns (user_reply, replied_to_list)
    """
    quotes = re.findall(r'<blockquote[^>]*>([\s\S]*?)</blockquote>', raw_content_html)
    replied_to = []
    
    for q in quotes:
        cite_m = re.search(r'<cite>(.*?)</cite>', q)
        cite_str = clean_html_text(cite_m.group(1)) if cite_m else ""
        
        q_body = re.sub(r'<cite>[\s\S]*?</cite>', ' ', q)
        q_text = clean_html_text(q_body)
        if q_text:
            replied_to.append({
                "cite": cite_str,
                "text": q_text
            })
            
    user_reply_html = raw_content_html
    while '<blockquote' in user_reply_html:
        u_new = re.sub(r'<blockquote[^>]*>[\s\S]*?</blockquote>', ' ', user_reply_html)
        if u_new == user_reply_html:
            break
        user_reply_html = u_new
        
    user_reply = clean_html_text(user_reply_html)
    return user_reply, replied_to

def fetch_page_with_retry(author_id, start=0, max_retries=3):
    """Fetches a page, handling phpBB search flood limits."""
    url = f"https://newmitbbs.com/search.php?st=0&sk=t&sd=d&sr=posts&author_id={author_id}&start={start}"
    req = urllib.request.Request(url, headers=HEADERS)
    
    for attempt in range(max_retries):
        try:
            resp = urllib.request.urlopen(req, context=ctx, timeout=20).read().decode("utf-8", errors="replace")
            
            # Check for flood protection
            flood_m = re.search(r'对不起您现在不能使用搜索，请在\s*(\d+)\s*秒后重试', resp)
            if flood_m:
                wait_sec = int(flood_m.group(1)) + 1
                time.sleep(wait_sec)
                continue
                
            return resp
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(2)
            
    return ""

def parse_page(resp, author_id):
    """Parses posts, author name, and total match count from raw HTML."""
    total_matches = None
    m_count = re.search(r'搜索找到\s*(\d+)\s*个匹配', resp)
    if m_count:
        total_matches = int(m_count.group(1))
        
    parts = re.split(r'<div class="search post [^"]*">', resp)[1:]
    results = []
    author_name = ""
    
    for p in parts:
        if not author_name:
            auth_m = re.search(rf'author_id={author_id}[^>]*class="username[^>]*>([^<]+)</a>', p)
            if not auth_m:
                auth_m = re.search(rf'class="username[^>]*><a[^>]*author_id={author_id}[^>]*>([^<]+)</a>', p)
            if auth_m:
                author_name = auth_m.group(1).strip()
        
        forum_m = re.search(r'版面[：:\s]*<a[^>]*>(.*?)</a>', p)
        forum = forum_m.group(1).strip() if forum_m else "综合"
        
        pb_m = re.search(r'<div class="postbody">([\s\S]*?)(?:<ul class="searchresults">|<div class="back2top">|<hr class="divider"|$)', p)
        if not pb_m:
            continue
        pb = pb_m.group(1)
        
        title_m = re.search(r'<h3><a[^>]*>(.*?)</a></h3>', pb)
        title = clean_html_text(title_m.group(1)) if title_m else ""
        
        date_m = re.search(r'<dd class="search-result-date">([^<]+)</dd>', p)
        date_str = date_m.group(1).strip() if date_m else ""
        
        content_m = re.search(r'<div class="content">([\s\S]*)', pb)
        if not content_m:
            continue
        raw_c = content_m.group(1)
        raw_c = re.sub(r'(?:</div>\s*)+$', '', raw_c.strip())
        
        user_reply, replied_to = parse_post_content(raw_c)
        post_type = "reply" if replied_to else "original_thread"
        
        results.append({
            "forum": forum,
            "title": title,
            "date": date_str,
            "post_type": post_type,
            "replied_to": replied_to,
            "user_reply": user_reply
        })
        
    return author_name, total_matches, results

def scrape_user(target_input, fetch_all=False, max_pages=10, output_path=None):
    author_id, preset_username = resolve_target(target_input)
    all_posts = []
    username = preset_username or ""
    
    print(f"[*] Initializing scrape for author_id: {author_id} (fetch_all={fetch_all})...")
    
    # 1. Fetch first page
    first_resp = fetch_page_with_retry(author_id, start=0)
    auth, total_matches, posts = parse_page(first_resp, author_id)
    
    if auth:
        username = auth
    if posts:
        all_posts.extend(posts)
        
    if total_matches is not None:
        total_pages = (total_matches + 19) // 20
        print(f"[+] Found {total_matches} total posts on forum across {total_pages} pages.")
    else:
        total_pages = 10
        print(f"[*] Total post count not detected. Using fallback.")

    if fetch_all:
        target_pages = total_pages
        print(f"[+] Full history requested: crawling all {target_pages} pages...")
    else:
        target_pages = min(max_pages, total_pages)
        print(f"[+] Sampling mode: crawling first {target_pages} pages ({target_pages*20} posts max).")
        
    if not output_path:
        user_tag = username if username else f"user_{author_id}"
        output_path = f"/tmp/mitbbs_{user_tag}.json"

    # 2. Iterate remaining pages
    if target_pages > 1:
        import concurrent.futures
        
        def fetch_single_page(idx):
            start_off = idx * 20
            try:
                p_resp = fetch_page_with_retry(author_id, start=start_off)
                p_auth, _, p_posts = parse_page(p_resp, author_id)
                return idx, p_auth, p_posts
            except Exception as ex:
                print(f"[!] Error fetching page {idx+1}: {ex}")
                return idx, None, []

        max_workers = 3 if target_pages > 10 else 1
        page_indices = list(range(1, target_pages))
        page_dict = {}
        completed = 0
        total_to_fetch = len(page_indices)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(fetch_single_page, idx): idx for idx in page_indices}
            for future in concurrent.futures.as_completed(future_to_idx):
                idx, p_auth, p_posts = future.result()
                if p_auth and not username:
                    username = p_auth
                page_dict[idx] = p_posts
                completed += 1
                if completed % 25 == 0 or completed == total_to_fetch:
                    pct = int((completed / total_to_fetch) * 100)
                    print(f"    Scraping progress: {completed}/{total_to_fetch} pages ({pct}%) fetched...")

        for idx in sorted(page_dict.keys()):
            all_posts.extend(page_dict[idx])

    if not username:
        username = f"user_{author_id}"

    forum_counter = Counter(p["forum"] for p in all_posts)
    result = {
        "author_id": author_id,
        "username": username,
        "total_matches_on_forum": total_matches,
        "total_posts_extracted": len(all_posts),
        "forum_distribution": dict(forum_counter.most_common()),
        "posts": all_posts
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        
    print(f"\n[+] Scrape completed successfully!")
    print(f"[+] Username: {username}")
    print(f"[+] Total Posts Extracted: {len(all_posts)} / {total_matches if total_matches else len(all_posts)}")
    print(f"[+] Output JSON: {output_path}")
    return result, output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scrape_posts.py <USERNAME_OR_URL_OR_ID> [OUTPUT_PATH] [--all] [--max-pages N]")
        sys.exit(1)
        
    target = sys.argv[1]
    out_file = None
    fetch_all_flag = False
    max_p = 10
    
    args = sys.argv[2:]
    for i, a in enumerate(args):
        if a == "--all":
            fetch_all_flag = True
        elif a == "--max-pages" and i + 1 < len(args):
            max_p = int(args[i+1])
        elif not a.startswith("-") and out_file is None:
            out_file = a
            
    scrape_user(target, fetch_all=fetch_all_flag, max_pages=max_p, output_path=out_file)
