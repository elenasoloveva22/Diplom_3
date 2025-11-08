from pages.base_page import BasePage
from pages.construct_page import Construct
from pages.profile_page import Profile
from pages.lenta_page import Lenta
import pytest
import allure
import time

class TestLentaPage():
    @allure.title("Проверка перехода в Ленту заказов через кнопку в шапке сайта")
    def test_lenta_button_click(self, driver, urls):
        base_page = BasePage(driver)
        base_page.get_urls(urls.STELLAR_BURGER_CONSTUCT)
        base_page.click_lenta_button()
        assert base_page.current_url(urls.STELLAR_BURGER_LENTA)

    @pytest.mark.parametrize("counter_method", ["get_all_time_order_count", "get_today_order_count"])
    @allure.title("Проверка увеличения счетчика заказов после создания нового заказа")
    def test_create_order_increases_counter(self, driver, login_user, urls, counter_method):
        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        lenta_page.get_urls(urls.STELLAR_BURGER_LENTA)
        count_before = getattr(lenta_page, counter_method)()
        construct_page.click_construct_button()
        profile_page.login_in_main_page(login_user["email"], login_user["password"])
        construct_page.add_bun_to_order() 
        construct_page.wait_for_order_number()
        construct_page.close_order_window()
        construct_page.wait_lenta_button_clickable()
        construct_page.click_lenta_button()
        construct_page.wait_url(urls.STELLAR_BURGER_LENTA)
        
        construct_page.wait(10) 
        driver.refresh()  
        construct_page.wait(3)  
        
        count_after = getattr(lenta_page, counter_method)()
        
        assert count_after > count_before, (
            f"Счетчик '{counter_method}' не увеличился: было {count_before}, стало {count_after}. "
            f"Разница: {count_after - count_before}"
        )

    @allure.title("Проверка добавления номера заказа в список 'В работе'")
    def test_create_order_list_order_add_number_order(self, driver, login_user, urls):
        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        construct_page.get_urls(urls.STELLAR_BURGER_LENTA)
        orders_before = lenta_page.get_order_list()
        construct_page.click_construct_button()
        profile_page.login_in_main_page(login_user["email"], login_user["password"])
        construct_page.add_bun_to_order() 
        construct_page.wait_for_order_number()
        initial_number = construct_page.get_order_number()
        construct_page.wait_for_order_number_changed(initial_number)
        number_order_modal = construct_page.get_order_number()
        number_order_normalized = number_order_modal.zfill(7)
        construct_page.close_order_window()
        construct_page.wait_lenta_button_clickable()
        construct_page.click_lenta_button()
        construct_page.wait_url(urls.STELLAR_BURGER_LENTA)
        
        construct_page.wait(10)
        driver.refresh()
        construct_page.wait(3)
        
        orders_after = lenta_page.get_order_list()
        construct_page.wait()
        assert number_order_normalized in orders_after