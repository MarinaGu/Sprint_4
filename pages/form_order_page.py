from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FormOrderPageLocators:
    LOCATOR_ORDER_FORM_NAME = (By.XPATH, ".//div/input[@placeholder='* Имя']")
    LOCATOR_ORDER_FORM_SERNAME = (By.XPATH, ".//div/input[@placeholder='* Фамилия']")
    LOCATOR_ORDER_FORM_ADRESS = (By.XPATH, ".//div/input[@placeholder='* Адрес: куда привезти заказ']")
    LOCATOR_ORDER_FORM_METRO = (By.XPATH, ".//div/input[@placeholder='* Станция метро']")
    LOCATOR_ORDER_FORM_METRO_CLICK = (By.XPATH, ".//div[@class='select-search__select']/ul/li/button/div[@class='Order_Text__2broi']")
    LOCATOR_ORDER_FORM_PHONE = (By.XPATH, ".//div/input[@placeholder='* Телефон: на него позвонит курьер']")
    LOCATOR_ORDER_FORM_NEXT_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")

    LOCATOR_ORDER_FORM_RENT_DATA = (By.XPATH, ".//div/input[@placeholder='* Когда привезти самокат']")
    LOCATOR_ORDER_FORM_RENT_PERIOD = (By.XPATH, ".//div/span[@class='Dropdown-arrow']")
    LOCATOR_ORDER_FORM_RENT_PERIOD_CLICK = (By.XPATH, ".//div/div/div[2]/div[2]/div[2]/div[2]/div[2]")
    LOCATOR_ORDER_FORM_RENT_COLOR = (By.XPATH, ".//div/div/label/input[@id='black']")
    LOCATOR_ORDER_FORM_RENT_COMMENT = (By.XPATH, ".//div/input[@placeholder='Комментарий для курьера']")
    LOCATOR_ORDER_FORM_RENT_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[2]")
    LOCATOR_ORDER_FORM_RENT_ORDER_OK_BUTTON = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']/div[@class='Order_Buttons__1xGrp']/button[2]")
    LOCATOR_ORDER_OK_TEXT = (By.XPATH, ".//div/div/div[@class='Order_Text__2broi']")
    LOCATOR_CLICK_STATUS_ORDER = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    LOCATOR_CLICK_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOCATOR_CLICK_YA = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

class FormOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.check_start_page = None

    def enter_name(self, name):
        form_order = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_NAME)
        form_order.send_keys(name)

    def enter_sername(self, sername):
        form_order = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_SERNAME)
        form_order.send_keys(sername)

    def enter_adress(self, adress):
        form_order = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_ADRESS)
        form_order.send_keys(adress)

    def enter_metro(self):
        form_order = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_METRO)
        form_order.click()
        form_order = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_METRO_CLICK)
        form_order.click()

    def enter_phone(self, phone):
        form_order = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_PHONE)
        form_order.send_keys(phone)

    def click_next_button(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_NEXT_BUTTON).click()

    def enter_data(self, data):
        form_rent = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_DATA)
        form_rent.send_keys(data)

    def enter_period(self):
        form_rent = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_PERIOD)
        form_rent.click()
        form_rent = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_PERIOD_CLICK)
        form_rent.click()

    def enter_color(self):
        form_rent = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_COLOR)
        form_rent.click()

    def enter_comment(self, comment):
        form_rent = self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_COMMENT)
        form_rent.send_keys(comment)

    def click_form_rent_order_button(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_ORDER_BUTTON).click()

    def click_order_ok_button(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_ORDER_FORM_RENT_ORDER_OK_BUTTON).click()

    def check_text_order(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_ORDER_OK_TEXT).text

    def click_look_status(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_CLICK_STATUS_ORDER).click()

    def click_scooter(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_CLICK_SCOOTER).click()

    def click_ya(self):
        return self.find_element(FormOrderPageLocators.LOCATOR_CLICK_YA).click()


