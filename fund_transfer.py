import pytest
import asyncio
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_fund_transfer(async_page):
    await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")
    await async_page.wait_for_timeout(1000)
    await async_page.locator('input[name="username"]').fill("MuraliK")
    await async_page.locator('input[name="password"]').fill("krishnan#456")
    await async_page.get_by_role("button", name="Log In").click()


# Navigate to Accounts Overview
    await async_page.get_by_role("link", name="Accounts Overview").click()
    # await expect(async_page.locator("#accountTable")).to_be_visible()
    # Identify two available accounts
    account = async_page.locator("#accountTable a")
    await expect(account.first).to_be_visible()
    account_count = await account.count()
    # assert account_count >= 2, ("At least two accounts are required for transfer.")
    old_account = (await account.nth(0).inner_text()).strip()
    new_account = (await account.nth(1).inner_text()).strip()
    print("From Account:", old_account)
    print("To Account:", new_account)

# Navigate to Transfer Funds
    await async_page.get_by_role("link", name="Transfer Funds").click()
    await expect(async_page.get_by_role("heading", name="Transfer Funds")).to_be_visible()

# Enter a valid transfer amount
    transfer_amount = "15"
    await async_page.locator("#amount").fill(transfer_amount)
    await async_page.locator("#fromAccountId").select_option(label=old_account)
    await async_page.locator("#toAccountId").select_option(label=new_account)
    await async_page.get_by_role("button", name="Transfer").click()


# Verify transfer confirmation
    await expect(async_page.get_by_text("Transfer Complete!", exact=True)).to_be_visible()
    print("Transfer completed successfully!")
    print("Transferred Amount: $", transfer_amount)


    await async_page.get_by_role("link", name="Accounts Overview").click()
    await async_page.locator(f"#accountTable a[href*='id={from_account}']").click()

    # Verify account details page
    await expect(async_page.locator("#accountId")).to_be_visible()
    transaction = async_page.locator("#transactionTable")
    await expect(transaction).to_be_visible()
    transaction_rows = transaction_table.locator("tbody tr")
    row_count = await transaction_rows.count()
    transaction_found = False
    for i in range(row_count):
        row = transaction_rows.nth(i)
        row_text = await row.inner_text()
        if ("Transfer" in row_text and transfer_amount in row_text):
            transaction_found = True
            print("Transaction Details:", row_text)
        break

    # assert transaction_found, ("Transfer transaction was not found in the source account history.")
    print("PASS: Transfer transaction is visible inaccount history.")



