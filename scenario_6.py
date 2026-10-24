import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_add_product_by_name(async_page):
    await async_page.goto("https://www.amazon.in/", wait_until="domcontentloaded")
    await async_page.locator("//input[@id='twotabsearchtextbox']").fill("the princess and the pea book")
    await async_page.locator("//input[@id='nav-search-submit-button']").click()
    await async_page.wait_for_timeout(1000)
    product = await async_page.locator("//h2[@aria-label='The Princess And The Pea']").inner_text()
    price = await async_page.locator("(//span[@class='a-price-whole'])[5]").inner_text()
    await async_page.locator("(//input[@name='submit.addToCart'])[2]").click()
    await async_page.wait_for_timeout(2000)
    print("Product added to cart successfully")
    print(f"Product selected: {product}")
    print(f"Product price: {price}")
