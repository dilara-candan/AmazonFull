import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class WishListPage(BasePage):
    WISH_LIST_CHECK = (By.CSS_SELECTOR, '#item-page-wrapper li')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[name="submit.deleteItem"]')

    def is_present_wish_list(self, productName):
        isPresentWishList = False
        self.PRODUCT_ITEM = (By.CSS_SELECTOR, 'a[title*="' + productName + '"]')

        for element in self.find_elements(*self.WISH_LIST_CHECK):
            try:
                if (element.find_element(*self.PRODUCT_ITEM)):
                    isPresentWishList = True
                    element.find_element(*self.DELETE_BUTTON).click()
                    time.sleep(2)
                    break
            except NoSuchElementException:
                pass

        return isPresentWishList

    def is_removed_item(self, productName):
        isRemovedItem = True
        self.REMOVED_PRODUCT_ITEM = (By.CSS_SELECTOR, '#item-page-wrapper li a[title*="' + productName + '"]')

        try:
            if (self.find_element(*self.REMOVED_PRODUCT_ITEM)):
                isRemovedItem = False
        except NoSuchElementException:
            pass

        return isRemovedItem
