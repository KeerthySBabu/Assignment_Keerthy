import pytest
import asyncio
from playwright.async_api import async_playwright, expect


@pytest.mark.asyncio
async def test_add_cart(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/", wait_until="domcontentloaded")
    
    category=  async_page.locator("(//a[@href='/books'])[1]")
    await category.click()
    await async_page.wait_for_timeout(1000)
    product = async_page.locator("(//input[@value='Add to cart'])[2]")
    await product.click()
    await async_page.wait_for_timeout(1000)
    pop_up = async_page.locator("//div[@class='bar-notification success']")
    await expect(pop_up).to_have_text("The product has been added to your shopping cart")
    print("Product added to cart successfully")

    
    
