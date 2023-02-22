from selenium.webdriver.common.by import By

from base_page import BasePage

class StartPageLocators:
    LOCATOR_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    LOCATOR_ORDER_FORM_NAME = (By.XPATH, ".//div/input[@placeholder='* Имя']")
    LOCATOR_ORDER_FORM_SERNAME = (By.XPATH, ".//div/input[@placeholder='* Фамилия']")
    LOCATOR_ORDER_FORM_ADRESS = (By.XPATH, ".//div/input[@placeholder='* Адрес: куда привезти заказ']")
    LOCATOR_ORDER_FORM_METRO = (By.XPATH, ".//div/input[@placeholder='* Станция метро']")
    LOCATOR_ORDER_FORM_PHONE = (By.XPATH, ".//div/input[@placeholder='* Телефон: на него позвонит курьер']")
    LOCATOR_ORDER_FORM_NEXT_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")
    LOCATOR_ORDER_FORM_RENT_DATA = (By.XPATH, ".//div/input[@placeholder='* Когда привезти самокат']")
    LOCATOR_ORDER_FORM_RENT_PERIOD = (By.XPATH, ".//div/div[@class='Dropdown-placeholder']")
    LOCATOR_ORDER_FORM_RENT_COLOR = (By.XPATH, ".//div/div/label/input[@id='black']")
    LOCATOR_ORDER_FORM_RENT_COMMENT = (By.XPATH, ".//div/input[@placeholder='Комментарий для курьера']")
    LOCATOR_ORDER_FORM_RENT_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[2]")
    LOCATOR_ORDER_FORM_RENT_ORDER_OK_BUTTON = (By.XPATH, ".//div/div[@class='Order_Buttons__1xGrp']/button[2]")
    LOCATOR_ORDER_OK_TEXT = (By.XPATH, ".//div/div/div[@class='Order_Text__2broi']")

class StartPage(BasePage):
    def click_order_button(self):
        order_button = self.find_element(StartPageLocators.LOCATOR_ORDER_BUTTON)
        order_button.click()

    def enter_form_order(self, name, sername, adress, metro, phone):
        form_order = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_NAME)
        form_order.send_kyes(name)
        form_order = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_SERNAME)
        form_order.send_kyes(sername)
        form_order = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_ADRESS)
        form_order.send_kyes(adress)
        form_order = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_METRO)
        form_order.send_kyes(metro)
        form_order = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_PHONE)
        form_order.send_kyes(phone)

    def click_next_button(self):
        next_button = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_NEXT_BUTTON)
        next_button.click()

    def enter_form_rent(self, data, period, color, comment):
        form_rent = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_RENT_DATA)
        form_rent.send_keys(data)
        form_rent = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_RENT_PERIOD)
        form_rent.send_keys(period)
        form_rent = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_RENT_COLOR)
        form_rent.send_keys(color)
        form_rent = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_RENT_COMMENT)
        form_rent.send_keys(comment)

    def click_form_order_button(self):
        form_order_ok = self.find_element(StartPageLocators.LOCATOR_ORDER_FORM_RENT_ORDER_BUTTON)
        form_order_ok.click()
