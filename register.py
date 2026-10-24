import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_register(async_page):
    Base_url = "https://parabank.parasoft.com/parabank"
    end_point = "register.htm"
    username = "MuraliK"
    password = "krishnan#456"
    await async_page.goto(Base_url+"/"+end_point)

    await async_page.locator("#customer\\.firstName").fill("Murali")
    await async_page.locator("#customer\\.lastName").fill("krishnan")
    await async_page.locator("#customer\\.address\\.street").fill("Palluruthy")
    await async_page.locator("#customer\\.address\\.city").fill("Kochi")
    await async_page.locator("#customer\\.address\\.state").fill("Kerala")
    await async_page.locator("#customer\\.address\\.zipCode").fill("682006")
    await async_page.locator("#customer\\.phoneNumber").fill("7736868955")
    await async_page.locator("#customer\\.ssn").fill("123456789")
    await async_page.locator("#customer\\.username").fill(username)
    await async_page.locator("#customer\\.password").fill(password)
    await async_page.locator("#repeatedPassword").fill(password)

    await async_page.locator("input[value='Register']").click()
    await async_page.wait_for_timeout(1000)

    # Verify registration result
    await expect(async_page.locator("#rightPanel")).to_contain_text("successfully", ignore_case=True)
    print("Registered customer :", username)

    #Verify egistered user is logged in
    await expect(async_page.locator("#leftPanel")).to_contain_text("Welcome", ignore_case=True)
    print("Registered user is logged in successfully")

    #accounts Overview page
    await async_page.locator("//a[@href='overview.htm']").click()
    await async_page.wait_for_timeout(1000)
    #verify one account is created
    # await expect(async_page.locator("//h1[@class='title']")).to_contain_text("Account Overview", ignore_case=True)
    print("Account details are displayed successfully")


    #logout
    await async_page.locator("//a[@href='logout.htm']").click()
    await async_page.wait_for_timeout(1000)
    print("User logged out")









    