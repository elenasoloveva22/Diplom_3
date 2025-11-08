from selenium.webdriver.common.by import By

class LentaPageLocators():

    COUNT_ALL_TIME = (By.XPATH, './/div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]') # Количество заказов за все время

    COUNT_TO_DAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Количество заказов за сегодня

    LIST_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]") # Список заказов в работе