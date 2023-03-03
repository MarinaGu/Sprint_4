from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class YaMainLocators:
    LOCATOR_YA_SEARCH_BUTTON = (By.XPATH, "//html/body/form/button[@class='arrow__button']")

class MainPage(BasePage):
    def text_on_search_button(self):
        return self.find_element(YaMainLocators.LOCATOR_YA_SEARCH_BUTTON).text

