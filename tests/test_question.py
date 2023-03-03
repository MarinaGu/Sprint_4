import allure
from pages.form_order_page import FormOrderPage
from pages.start_page import StartPage

@allure.story("tests")
@allure.feature('test question')
def test_how_many(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    how_many_text = start_page.how_many_rent()
    assert 'Сутки' and 'рублей' in how_many_text

def test_moore_scooter(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    more_scooter_text = start_page.more_scooter()
    assert 'заказ' and 'самокат' in more_scooter_text


def test_time_rent(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    time_rent_text = start_page.time_rent()
    assert 'оплатите заказ курьеру' in time_rent_text

def test_scooter_to_day(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    scooter_to_day_text = start_page.scooter_to_day()
    assert 'начиная с завтрашнего' in scooter_to_day_text

def test_long_order(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    long_order_text = start_page.long_order()
    assert 'Пока что нет' in long_order_text


def test_power_scooter(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    power_scooter_text = start_page.power_scooter()
    assert 'полной зарядкой' in power_scooter_text

def test_cancel_order(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    cancel_order_text = start_page.cancel_order()
    assert 'пока самокат не привезли' in cancel_order_text

def test_where_delivery(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    start_page.scroll_into_view_FAQ_elements()

    where_delivery_text = start_page.where_delivery()
    assert 'Всем самокатов!' in where_delivery_text
