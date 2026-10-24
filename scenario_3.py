import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_add_product_by_price(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
    
    await async_page.locator("(//a[@href='/books'])").first.click()
    await async_page.wait_for_timeout(1000)
    amount = "10.00"
    price = async_page.locator(f"(//span[@class='price actual-price' and text()= '{amount}'])[3]")
    await expect(price).to_have_text(amount)
    product_name = await async_page.locator(f"(//h2[@class='product-title'])[5]").inner_text()
    print(f"Product selected: {product_name}")
    print(f"Product price: {amount}")
    await async_page.wait_for_timeout(1000)
