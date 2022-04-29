import unittest
from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestHomePage(BaseTest):

    # def test_search_form(self):
    #     # Step01: Navigate to Home Page
    #     home_page = HomePage(self.driver)
    #
    #     # Step02: Enter 'Trà sữa kem tươi' into search text box
    #     home_page.search_beverage_name("Trà sữa Kem tươi")

        # Step03: Save screen shoot
        # home_page.save_screen_shoot("../capture_screen/test_search_form/test_search_form.png")

    # def test_order_beverage(self):
    #     # Step01: Navigate to Home Page
    #     home_page = HomePage(self.driver)
    #
    #     # Step02: Choose "Trà sữa trân châu đường đen size M",
    #     # "Trà sữa trân châu đường đen size L", "Trà sữa trân châu thái" in menu
    #     home_page.click_to_choose_tstcdd_size_m()
    #     home_page.click_to_choose_tstcdd_size_l()
    #     home_page.click_to_choose_tstx()
    #
    #     # Step03: Save screen shoot
    #     home_page.save_screen_shoot("../capture_screen/test_order_beverage/test_order_beverage.png")
    #
    #     # Step 04: Check calculated bill
    #     total_price_of_beverages = home_page.get_total_price_of_beverages_text_result()
    #     assert total_price_of_beverages == "82,450 VND"
    #
    #     discount_bill = home_page.get_discount_text_result()
    #     assert discount_bill == "7,918 VND"
    #
    #     total_price = home_page.get_total_price_text_result()
    #     assert total_price == "74,532 VND"

    # def test_change_quantity_of_beverage(self):
    #     # Step01: Navigate to Home Page
    #     home_page = HomePage(self.driver)
    #
    #     # Step02: Choose "Trà sữa trân châu đường đen size M" and "Trà sữa trân xoài" in menu
    #     home_page.click_to_choose_tstcdd_size_m()
    #     home_page.click_to_choose_tstx()
    #
    #     # Step03: Increase quantity of "Trà sữa trân châu đường đen size M" 5 times, after that, decrease 2 times.
    #     # Increase quantity of "Trà sữa trân xoài" 3 times, after that, decrease 1 times.
    #     home_page.click_increase_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-1.png")
    #     home_page.click_increase_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-2.png")
    #     home_page.click_increase_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-3.png")
    #     home_page.click_increase_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-4.png")
    #     home_page.click_increase_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-5.png")
    #
    #     home_page.click_decrease_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-6.png")
    #     home_page.click_decrease_tstcdd_size_m_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-7.png")
    #
    #     home_page.click_increase_tstx_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-8.png")
    #     home_page.click_increase_tstx_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-9.png")
    #     home_page.click_increase_tstx_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-10.png")
    #
    #     home_page.click_decrease_tstx_quantity_button()
    #     home_page.save_screen_shoot("../capture_screen/test_change_quantity/image-11.png")

    def test_submit_receipt(self):
        # Step01: Navigate to Home Page
        home_page = HomePage(self.driver)

        # Step02: Choose "Trà sữa trân châu đường đen size M" and "Trà sữa trân xoài" in menu
        home_page.click_to_choose_tstcdd_size_m()
        home_page.click_to_choose_tstx()

        # Step03: Increase quantity of "Trà sữa trân châu đường đen size M" to 2.
        # Increase quantity of "Trà sữa trân xoài" to 3.
        home_page.click_increase_tstcdd_size_m_quantity_button()
        home_page.click_increase_tstcdd_size_m_quantity_button()
        home_page.click_increase_tstx_quantity_button()
        home_page.click_increase_tstx_quantity_button()
        home_page.click_increase_tstx_quantity_button()

        # Step04: Press "Đã thanh toán" button
        home_page.click_to_submit_receipt()

        # Step05: Check popup
        home_page.check_pop_up()
        home_page.save_screen_shoot("../capture_screen/test_submit_receipt/image.png")

if __name__ == '__main__':
    unittest.main()
