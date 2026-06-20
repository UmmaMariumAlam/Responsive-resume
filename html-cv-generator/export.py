from pathlib import Path

from playwright.sync_api import sync_playwright


BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = (BASE_DIR / "cv.html").resolve().as_uri()
PDF_FILE = BASE_DIR / "Umma_Marium_Alam_CV_Dark.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Load the local HTML file through a file:// URL.
    page.goto(HTML_FILE, wait_until="networkidle")
    
    # Generate PDF with DARK THEME preserved
    page.pdf(
        path=str(PDF_FILE),
        format="A4",
        print_background=True,
        margin={"top": "0.0cm", "bottom": "0.0cm", "left": "0.0cm", "right": "0.0cm"}
    )
    browser.close()
    print("PDF created successfully!")