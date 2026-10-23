import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_url():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
        # page.goto(BASE_URL)
        print("Page Title:", page.title())

        browser.close()
