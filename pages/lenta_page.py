import allure
from locators.lenta_page_locators import LentaPageLocators
from pages.base_page import BasePage

class Lenta(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("Получить общее количество заказов за все время")
    def get_all_time_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_ALL_TIME)
        return int(self.find_element(LentaPageLocators.COUNT_ALL_TIME).text)
    
    @allure.title("Получить количество заказов за сегодня")
    def get_today_order_count(self):
        self.wait_element(LentaPageLocators.COUNT_TO_DAY)
        return int(self.find_element(LentaPageLocators.COUNT_TO_DAY).text)
    
    @allure.title("Получить список номеров заказов")
    def get_order_list(self):
        self.wait_element(LentaPageLocators.LIST_ORDER)
        return [order.text for order in self.find_elements(LentaPageLocators.LIST_ORDER)]
    
    @allure.title("Проверить отображение списка заказов")
    def is_order_list_displayed(self):
        return self.element_is_displayed(LentaPageLocators.LIST_ORDER)