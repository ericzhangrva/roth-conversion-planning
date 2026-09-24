#!/usr/bin/env python3
"""
Renders PDF pages to high-resolution JPEG images and runs OCR text extraction.
"""

import sys, os, subprocess
import fitz # pymupdf
from PIL import Image

def process_pdf(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pages_dir = os.path.join(output_dir, "pages")
    ocr_dir = os.path.join(output_dir, "ocr_text")
    os.makedirs(pages_dir, exist_ok=True)
    os.makedirs(ocr_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    print(f"Loaded {pdf_path}: {len(doc)} pages.")

    # High resolution 2x scale
    zoom = 2.0
    mat = fitz.Matrix(zoom, zoom)

    for i, page in enumerate(doc):
        page_num = i + 1
        pix = page.get_pixmap(matrix=mat)
        img_path = os.path.join(pages_dir, f"page_{page_num:02d}.jpg")
        pix.save(img_path)
        print(f"Rendered Page {page_num:02d} -> {img_path}")

        # OCR using tesseract
        txt_out_prefix = os.path.join(ocr_dir, f"page_{page_num:02d}")
        cmd = ["tesseract", img_path, txt_out_prefix, "-l", "chi_sim+eng"]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  OCR completed -> {txt_out_prefix}.txt")

    print("All pages successfully rendered and transcribed.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 pdf_to_images.py <path_to_pdf> <output_dir>")
        sys.exit(1)
    process_pdf(sys.argv[1], sys.argv[2])
