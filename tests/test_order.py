import allure
from pages.ya_page import MainPage
from pages.form_order_page import FormOrderPage
from pages.start_page import StartPage


@allure.story("tests")
@allure.feature('test order')
def test_order_up_button(browser):
    start_page = StartPage(browser)
    form_order = FormOrderPage(browser)

    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.click_order_up_button()
    form_order.enter_name("Имя")
    form_order.enter_sername("Фамилия")
    form_order.enter_adress("Адрес")
    form_order.enter_metro()
    form_order.enter_phone("89113456789")
    form_order.click_next_button()
    form_order.enter_data("21.03.2023")
    form_order.enter_period()
    form_order.enter_color()
    form_order.enter_comment("")
    form_order.click_form_rent_order_button()
    form_order.click_order_ok_button()
    order_text = form_order.check_text_order()
    assert "Номер заказа" in order_text
    form_order.click_look_status()
    form_order.click_scooter()
    check_text = start_page.check_start_page()
    assert "Самокат" in check_text

def test_order_down_button(browser):
    start_page = StartPage(browser)
    form_order = FormOrderPage(browser)
    ya_page = MainPage(browser)

    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.click_order_down_button()

    form_order.enter_name("Петя")
    form_order.enter_sername("Петров")
    form_order.enter_adress("Москва")
    form_order.enter_metro()
    form_order.enter_phone("89113452345")
    form_order.click_next_button()
    form_order.enter_data("26.04.2023")
    form_order.enter_period()
    form_order.enter_color()
    form_order.enter_comment("")
    form_order.click_form_rent_order_button()
    form_order.click_order_ok_button()
    order_text = form_order.check_text_order()
    assert "Номер заказа" in order_text

    form_order.click_look_status()
    form_order.click_ya()
    check_text = ya_page.text_on_search_button()
    assert "Найти" == check_text