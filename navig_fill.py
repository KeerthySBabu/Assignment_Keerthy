import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio

async def test_fill():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        async_page = await browser.new_page()

        await async_page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")

        search_box = async_page.locator("//input[@id='small-searchterms']")
        await search_box.click()
        await search_box.fill("Mobiles")
        submit = async_page.locator("//input[@class='button-1 search-box-button']")
        await submit.click()

        print("Page Title:", await async_page.title())
        print("Search field filled successfully")

        
        
