from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_LIST_BUTTON = (By.ID, 'wishListMainButton')
    WISH_LIST = (By.ID, 'huc-view-your-list-button')
    WISH_LIST_ITEM = (By.CSS_SELECTOR, "span#productTitle")

    def click_add_list(self):
        self.click_element(*self.ADD_LIST_BUTTON)

    def click_wish_list(self):
        self.click_element(*self.WISH_LIST)

    def get_product_name(self):
        return self.find_element(*self.WISH_LIST_ITEM).text[0:25]
