from pages.base_page import BasePage
from utils.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super(HomePage, self).__init__(driver)

    def search_beverage_name(self, keyword):
        # self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_element_located(self.locator.TRA_SUA_KEM_TUOI))
        self.find_element(*self.locator.SEARCH_INPUT).send_keys(keyword)

    def click_to_choose_tstcdd_size_m(self):
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.locator.TRA_SUA_TRAN_CHAU_DUONG_DEN_SIZE_M))
        self.find_element(*self.locator.TRA_SUA_TRAN_CHAU_DUONG_DEN_SIZE_M).click()

    def click_to_choose_tstcdd_size_l(self):
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.locator.TRA_SUA_TRAN_CHAU_DUONG_DEN_SIZE_L))
        self.find_element(*self.locator.TRA_SUA_TRAN_CHAU_DUONG_DEN_SIZE_L).click()

    def click_to_choose_tstx(self):
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.locator.TRA_SUA_TRAN_XOAI))
        self.find_element(*self.locator.TRA_SUA_TRAN_XOAI).click()

    def click_to_change_beverage_quantity(self, beverage_locator):
        self.find_element(beverage_locator).click()

    def click_to_clear_receipt(self):
        self.find_element(*self.locator.CLEAR_RECEIPT_BUTTON).click()

    def click_to_submit_receipt(self):
        self.find_element(*self.locator.SUBMIT_RECEIPT_BUTTON).click()

    def check_pop_up(self):
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(self.locator.SUBMIT_POPUP))

    def get_total_price_of_beverages_text_result(self):
        return self.find_element(*self.locator.TOTAL_PRICE_OF_ALL_BEVERAGES).text

    def get_discount_text_result(self):
        return self.find_element(*self.locator.DISCOUNT_BILL).text

    def get_total_price_text_result(self):
        return self.find_element(*self.locator.TOTAL_PRICE).text

    def click_increase_tstcdd_size_m_quantity_button(self):
        self.find_element(*self.locator.INCREASE_TSTCDD_SIZE_M_QUANTITY_BUTTON).click()

    def click_decrease_tstcdd_size_m_quantity_button(self):
        self.find_element(*self.locator.DECREASE_TSTCDD_SIZE_M_QUANTITY_BUTTON).click()

    def click_increase_tstx_quantity_button(self):
        self.find_element(*self.locator.INCREASE_TSTX_QUANTITY_BUTTON).click()

    def click_decrease_tstx_quantity_button(self):
        self.find_element(*self.locator.DECREASE_TSTX_QUANTITY_BUTTON).click()