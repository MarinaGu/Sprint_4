import allure
import pytest
from pages.ya_page import MainPage
from pages.form_order_page import FormOrderPage
from pages.start_page import StartPage


@allure.story("tests")
@allure.feature('test order')
@pytest.mark.parametrize('name, sername, adress, phone, data, comment', [['Иван', 'Иванов', 'Москва', '891134567824', '23.03.2023', 'утром'], ['Петр', 'Петров', 'Москва, Сокольники', '89124568932', '31.03.2023', ' ']])

def test_order_up_button(browser, name, sername, adress, phone, data, comment):
    start_page = StartPage(browser)
    form_order = FormOrderPage(browser)

    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.click_order_up_button()
    form_order.enter_name(name)
    form_order.enter_sername(sername)
    form_order.enter_adress(adress)
    form_order.enter_metro()
    form_order.enter_phone(phone)
    form_order.click_next_button()
    form_order.enter_data(data)
    form_order.enter_period()
    form_order.enter_color()
    form_order.enter_comment(comment)
    form_order.click_form_rent_order_button()
    form_order.click_order_ok_button()
    order_text = form_order.check_text_order()
    assert "Номер заказа" in order_text
    form_order.click_look_status()
    form_order.click_scooter()
    check_text = start_page.check_start_page()
    assert "Самокат" in check_text

@pytest.mark.parametrize('name, sername, adress, phone, data, comment', [['Аркадий', 'Захаров', 'Красная площадь', '89234567894', '28.04.2023', 'днем'], ['Дмитрий', 'круглов', 'Москва', '89654321785', '18.03.2023', ' ']])
def test_order_down_button(browser, name, sername, adress, phone, data, comment):
    start_page = StartPage(browser)
    form_order = FormOrderPage(browser)
    ya_page = MainPage(browser)

    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.click_order_down_button()

    form_order.enter_name(name)
    form_order.enter_sername(sername)
    form_order.enter_adress(adress)
    form_order.enter_metro()
    form_order.enter_phone(phone)
    form_order.click_next_button()
    form_order.enter_data(data)
    form_order.enter_period()
    form_order.enter_color()
    form_order.enter_comment(comment)
    form_order.click_form_rent_order_button()
    form_order.click_order_ok_button()
    order_text = form_order.check_text_order()
    assert "Номер заказа" in order_text

    form_order.click_look_status()
    form_order.click_ya()
    check_text = ya_page.text_on_search_button()
    assert "Найти" == check_text