import pytest
import asyncio
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_open_new_account(async_page):
    await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")
    await async_page.wait_for_timeout(1000)
    await async_page.locator('input[name="username"]').fill("MuraliK")
    await async_page.locator('input[name="password"]').fill("krishnan#456")
    await async_page.get_by_role("button", name="Log In").click()



# Navigate to Open New Account
    await async_page.get_by_role("link", name="Open New Account").click()
    await expect(async_page.get_by_role("heading", name="Open New Account")).to_be_visible()

# Select account type
    await async_page.locator("#type").select_option(label="SAVINGS")
    account =async_page.locator("#fromAccountId")
    await expect(account.locator("option").first).to_be_attached()
    old_account_number = await account.locator("option").first.get_attribute("value")
    assert old_account_number, ("No existing account is available.")
    await account.select_option(value=old_account_number)


#Open the new account
    await async_page.get_by_role("button", name="Open New Account").click()
    await expect(async_page.get_by_text("Account Opened!", exact=True)).to_be_visible()

# Capture the generated account number
    new_account_link = async_page.locator("#newAccountId")
    await expect(new_account_link).to_be_visible()
    new_account_number = (await new_account_link.inner_text()).strip()

    assert new_account_number, ("New account number was not generated.")
    print("New account created successfully!")
    print("Existing Account:", old_account_number)
    print("New Account Number:", new_account_number)

#Navigate to Accounts Overview
    await async_page.get_by_role("link", name="Accounts Overview").click()
    
    
# Verify the new account is displayed
    account_link = async_page.locator("#accountTable a").filter(has_text=new_account_number)
    await expect(account_link).to_be_visible()
    print("PASS: New account is displayed in Accounts Overview.")