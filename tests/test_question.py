from pages.form_order_page import FormOrderPage
from pages.start_page import StartPage

def test_questions(browser):
    start_page = StartPage(browser)
    start_page.go_to_site()
    start_page.click_cookie_button()
    #start_page.scroll_into_view_FAQ_elements()

    how_many_text = start_page.how_many_rent()
    assert 'Сутки' and 'рублей' in how_many_text

    more_scooter_text = start_page.more_scooter()
    assert 'заказ' and 'самокат' in more_scooter_text

    time_rent_text = start_page.time_rent()
    assert 'оплатите заказ курьеру' in time_rent_text

    scooter_to_day_text = start_page.scooter_to_day()
    assert 'начиная с завтрашнего' in scooter_to_day_text

    long_order_text = start_page.long_order()
    assert 'Пока что нет' in long_order_text

    power_scooter_text = start_page.power_scooter()
    assert 'полной зарядкой' in power_scooter_text

    cancel_order_text = start_page.cancel_order()
    assert 'пока самокат не привезли' in cancel_order_text

    where_delivery_text = start_page.where_delivery()
    assert 'Всем самокатов!' in where_delivery_text
