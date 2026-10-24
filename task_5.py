import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio

async def test_locate_click_fill_press(async_page):
    await async_page.goto("https://www.nykaa.com/", wait_until="domcontentloaded")
    await async_page.get_by_label("Mobile Number").fill("7736863255")
    await async_page.wait_for_timeout(1000)
    await async_page.get_by_role("button", name="Send OTP").press("Enter")
    await async_page.wait_for_timeout(1000)
    print("OTP sent successfully")