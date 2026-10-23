from playwright.sync_api import sync_playwright


def test_firefox():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")
        print("Firefox Page Title:", page.title())

        browser.close()