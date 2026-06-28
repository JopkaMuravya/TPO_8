from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.XPATH, "//button[text()='Remove']")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def add_backpack(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)