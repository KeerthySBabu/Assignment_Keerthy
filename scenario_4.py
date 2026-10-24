import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_add_product_by_name(async_page):
    await async_page.goto("https://www.amazon.in/", wait_until="domcontentloaded")
    await async_page.locator("//input[@id='twotabsearchtextbox']").fill("books")
    await async_page.locator("//input[@id='nav-search-submit-button']").click()
    product =async_page.locator("(//span[@class='a-truncate-full a-offscreen'])[2]")
    await expect(product).to_be_visible()
    name = await product.inner_text()
    print(f"Product Name: {name}")
    price = async_page.locator("(//span[@class='a-price-whole'])[1]")
    await expect(price).to_be_visible()
    price_value = await price.inner_text()
    print(f"Product Price: {price_value}")
