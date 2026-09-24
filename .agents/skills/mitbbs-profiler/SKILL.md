---
name: mitbbs-profiler
description: >-
  Automatically analyzes and generates a comprehensive user persona (用户形象) for any user
  on NewMitBBS (newmitbbs.com). Use this skill whenever the user provides a link to an author's
  post history, profile page, or author ID on MITBBS, and requests a persona analysis,
  demographic breakdown, or output to an ID text file (e.g. id.txt or <username>.txt).
---

# MITBBS User Profiler (用户形象画像分析器)

This skill automates the end-to-end process of scraping, isolating, analyzing, and synthesizing a comprehensive user persona (用户形象) for any forum member on NewMitBBS (`newmitbbs.com`).

---

## Workflow Steps

### Step 1: Run the Extraction Script
When the user provides a **Username** (e.g., `foxbat`, `coolcat`, `牛河梁`), a **URL**, or a numeric `author_id`:

Execute the extraction helper script:
```bash
# Standard recent sampling (up to 200 posts) by Username or URL:
python3 /Users/eric/Dropbox/ai/mitbbs-profiler/scripts/scrape_posts.py "<USERNAME_OR_URL_OR_ID>" /tmp/mitbbs_user.json

# OR for full historical extraction (crawls all posts automatically):
python3 /Users/eric/Dropbox/ai/mitbbs-profiler/scripts/scrape_posts.py "<USERNAME_OR_URL_OR_ID>" /tmp/mitbbs_user.json --all
```

This script:
1. Automatically resolves usernames (e.g. `coolcat` $\rightarrow$ `author_id: 16040`) or parses URLs.
2. Fetches up to 200 recent posts across pages with proper headers and SSL handling.
3. **Strictly separates quotes from original replies**:
   - `replied_to`: Text written by *other* users that this ID was replying to.
   - `user_reply`: The target user's *actual* original text.
   *(CRITICAL: Never attribute quoted text to the ID being analyzed!)*
4. Detects the forum username, post dates, and board distribution.
5. Saves the parsed data with this clean separation to `/tmp/mitbbs_user.json`.

---

### Step 2: Ingest & Filter Post History
Read `/tmp/mitbbs_user.json`. Inspect the posts and categorize them across key behavioral and thematic dimensions:
* **Demographics & Generation:** Look for self-references (e.g., “叔”, “老牛”, “53”), graduation decade (80s/90s), references to college dorms, and current location in the US (state/city).
* **Family & Life Stage:** Mentions of spouse (“廉颇”), children (“娃”, schools, colleges, activities), elderly parents (“老人”, “养老院”, domestic visits).
* **Financial & Assets:** Mentions of retirement accounts (401k, Roth), investments, home purchases, property taxes, spending habits.
* **Political & Geopolitical Views:** Stance on CCP/China, US politics, Russia-Ukraine, Taiwan, overseas vs. domestic commentary.
* **Domain Expertise & Hobbies:** Automotive preferences (engine types, car brands), tech/AI, firearms, cinema, sports, home repair/DIY.
* **Tone & Language Style:** Sarcasm, humor, slang, temperament, combativeness on forum threads.

---

### Step 3: Write the Detailed Profile Report (`<username>.txt`)
Generate a deeply insightful, structured report in **Chinese** and write it directly to the user's workspace file named after the user's ID:
* Target filename: `<username>.txt` (e.g. `coolcat.txt`, `foxbat.txt`). Each user gets their own dedicated file so profiles are never overwritten.

The report must follow this standard multi-dimensional framework:
1. **基本人口学特征（Demographics & Background）**: 年龄代际、留美年限、地理坐标、教育背景与专业特长。
2. **经济与财富画像（Financial Profile & Asset Management）**: 资产阶层、消费观念、投资偏好、退休规划与财税意识。
3. **家庭与生活状态（Family & Lifestyle）**: 婚姻与子女现状、父母养老状况、动手能力与日常生活情趣。
4. **行业背景与专业思维（Professional Mindset & Domain Traits）**: 职业痕迹、工程逻辑、决策直觉。
5. **政治立场与意识形态（Political & Ideological Stance）**: 政治光谱、对涉华/涉美/地缘议题的核心观点。
6. **消费品味与个人兴趣（Consumer Taste & Hobbies）**: 选车哲学、电子数码、文化影视、特殊爱好（如枪械、DIY、户外等）。
7. **语言风格与网络人格画像（Tone & Persona Summary）**: 自称、口头禅、对线风格与人设总结。

---

### Step 4: Present Summary to User
Provide the user with:
1. The extracted username and post count analyzed.
2. A crisp, bulleted executive summary of the persona.
3. A direct clickable link to the generated text file: `[<filename>.txt](file:///absolute/path/to/<filename>.txt)`.
