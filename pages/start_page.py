from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class StartPageLocators:
    LOCATOR_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    LOCATOR_SCOOTER_TEXT = (By.XPATH, ".//div[@class='Home_HomePage__ZXKIX']/div/div[@class='Home_Header__iJKdX']")

    #локаторы для заказа самоката
    LOCATOR_ORDER_UP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    LOCATOR_ORDER_DOWN_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button")#(By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")

    #локаторы для проверка вопросов о важном
    LOCATOR_ACCORDION = (By.CLASS_NAME, "accordion")
    LOCATOR_QU_HOW_MANY_RENT = (By.XPATH, ".//div[@id='accordion__heading-0']")
    LOCATOR_QU_MORE_SCOOTER = (By.XPATH, ".//div[@id='accordion__heading-1']")
    LOCATOR_QU_TIME_RENT = (By.XPATH, ".//div[@id='accordion__heading-2']")
    LOCATOR_QU_SCOOTER_TO_DAY = (By.XPATH, ".//div[@id='accordion__heading-3']")
    LOCATOR_QU_LONG_ORDER = (By.XPATH, ".//div[@id='accordion__heading-4']")
    LOCATOR_QU_POWER_SCOOTER = (By.XPATH, ".//div[@id='accordion__heading-5']")
    LOCATOR_QU_CANCEL_ORDER = (By.XPATH, ".//div[@id='accordion__heading-6']")
    LOCATOR_QU_WHERE_DELIVERY = (By.XPATH, ".//div[@id='accordion__heading-7']")

    #локаторы ответов на вопросы
    LOCATOR_ANS_HOW_MANY_RENT = (By.XPATH, ".//div[@id='accordion__panel-0']")
    LOCATOR_ANS_MORE_SCOOTER = (By.XPATH, ".//div[@id='accordion__panel-1']")
    LOCATOR_ANS_TIME_RENT = (By.XPATH, ".//div[@id='accordion__panel-2']")
    LOCATOR_ANS_SCOOTER_TO_DAY = (By.XPATH, ".//div[@id='accordion__panel-3']")
    LOCATOR_ANS_LONG_ORDER = (By.XPATH, ".//div[@id='accordion__panel-4']")
    LOCATOR_ANS_POWER_SCOOTER = (By.XPATH, ".//div[@id='accordion__panel-5']")
    LOCATOR_ANS_CANCEL_ORDER = (By.XPATH, ".//div[@id='accordion__panel-6']")
    LOCATOR_ANS_WHERE_DELIVERY = (By.XPATH, ".//div[@id='accordion__panel-7']")


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.LOCATOR_ACCORDION = (By.CLASS_NAME, "accordion")

    def click_cookie_button(self):
        return self.find_element(StartPageLocators.LOCATOR_COOKIE_BUTTON).click()

    def click_order_up_button(self):
        return self.find_element(StartPageLocators.LOCATOR_ORDER_UP_BUTTON).click()

    def click_order_down_button(self):
        return self.find_element(StartPageLocators.LOCATOR_ORDER_DOWN_BUTTON).click()

    def scroll_into_view_FAQ_elements(self):
        accordion_elements = self.driver.find_element(*self.LOCATOR_ACCORDION)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_elements)


    def check_start_page(self):
        return self.find_element(StartPageLocators.LOCATOR_SCOOTER_TEXT).text

    def how_many_rent(self):
        how_many = self.find_element(StartPageLocators.LOCATOR_QU_HOW_MANY_RENT)
        how_many.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_HOW_MANY_RENT).text

    def more_scooter(self):
        more_scooter = self.find_element(StartPageLocators.LOCATOR_QU_MORE_SCOOTER)
        more_scooter.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_MORE_SCOOTER).text

    def time_rent(self):
        time_rent = self.find_element(StartPageLocators.LOCATOR_QU_TIME_RENT)
        time_rent.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_TIME_RENT).text

    def scooter_to_day(self):
        scooter_to_day = self.find_element(StartPageLocators.LOCATOR_QU_SCOOTER_TO_DAY)
        scooter_to_day.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_SCOOTER_TO_DAY).text

    def long_order(self):
        long_order = self.find_element(StartPageLocators.LOCATOR_QU_LONG_ORDER)
        long_order.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_LONG_ORDER).text

    def power_scooter(self):
        power_scooter = self.find_element(StartPageLocators.LOCATOR_QU_POWER_SCOOTER)
        power_scooter.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_POWER_SCOOTER).text

    def cancel_order(self):
        cancel_order = self.find_element(StartPageLocators.LOCATOR_QU_CANCEL_ORDER)
        cancel_order.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_CANCEL_ORDER).text

    def where_delivery(self):
        where_delivery = self.find_element(StartPageLocators.LOCATOR_QU_WHERE_DELIVERY)
        where_delivery.click()
        return self.find_element(StartPageLocators.LOCATOR_ANS_WHERE_DELIVERY).text