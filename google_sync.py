from playwright.sync_api import sync_playwright


def test_chrome_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")
        print("Page Title:", page.title())

        browser.close()