import pytest
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("SauceDemo Tests")
class TestSauceDemo:

    @allure.story("Login Tests")
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url

    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("locked_out_user", "secret_sauce")
        assert "Sorry, this user has been locked out" in login_page.get_text(login_page.ERROR_MESSAGE)

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "wrong_pass")
        assert "Username and password do not match" in login_page.get_text(login_page.ERROR_MESSAGE)

    @allure.story("Inventory Tests")
    def test_add_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack()
        assert inventory_page.get_text(inventory_page.CART_BADGE) == "1"

    def test_remove_from_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack()
        inventory_page.click(inventory_page.REMOVE_BACKPACK)
        assert len(driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")) == 0

    def test_product_details_navigation(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
        assert "inventory-item.html" in driver.current_url

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        inventory_page.logout()
        assert driver.current_url == "https://www.saucedemo.com/"

    def test_cart_persistence(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_backpack()
        driver.refresh()
        assert inventory_page.get_text(inventory_page.CART_BADGE) == "1"

    def test_checkout_step_one(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        driver.get("https://www.saucedemo.com/checkout-step-one.html")
        assert "Checkout: Your Information" in driver.page_source

    def test_empty_login(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login("", "")
        assert "Username is required" in login_page.get_text(login_page.ERROR_MESSAGE)