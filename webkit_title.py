from playwright.sync_api import sync_playwright


def test_webkit():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")
        print("WebKit Page Title:", page.title())

        browser.close()
