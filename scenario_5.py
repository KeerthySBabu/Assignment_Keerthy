import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_add_product_by_rating(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
    
    await async_page.locator("(//a[@href='/jewelry'])").first.click()
    await async_page.wait_for_timeout(1000)
    name = await async_page.locator(f"(//a[@href='/black-white-diamond-heart'])[2]").inner_text()
    print(f"Product selected: {name}")
    await async_page.wait_for_timeout(1000)
    rating =async_page.locator("(//div[@class='product-rating-box' and @title='643 review(s)'])")
    print(f"Product rating: {await rating.get_attribute('title')}")
    await async_page.wait_for_timeout(1000)
