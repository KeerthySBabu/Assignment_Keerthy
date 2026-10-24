import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_navigate_left(async_page):
    await async_page.goto("https://www.amazon.in/", wait_until="domcontentloaded")
    left_nav = async_page.locator("//i[@class='hm-icon nav-sprite']")
    await left_nav.click()
    await async_page.wait_for_timeout(1000)
    headers = async_page.locator("//div[@class='hmenu-item hmenu-title ']")
    count = await headers.count()
    print(f"Left navigation headers: {count}")

    for i in range(count):
        heading = (await headers.nth(i).inner_text()).strip()
        if heading:
            print(heading)