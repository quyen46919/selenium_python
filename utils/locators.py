from selenium.webdriver.common.by import By


class MainPageLocators(object):

    SHOW_ALL_ITEMS_BUTTON = (By.CSS_SELECTOR, '.pos__list-item--li button.active')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.pos__list-item--input')
    CLEAR_RECEIPT_BUTTON = (By.CSS_SELECTOR, '.pos__current-order button')
    SHIP_FEE_INPUT = (By.ID, 'shipping-fee')
    SUBMIT_RECEIPT_BUTTON = (By.CSS_SELECTOR, '.pos__bill button.pos__submit')

    TOTAL_PRICE_OF_ALL_BEVERAGES = (By.ID, "totalPrice")
    DISCOUNT_BILL = (By.CSS_SELECTOR, ".pos__discount")
    TOTAL_PRICE = (By.ID, "finalPrice")

    TRA_SUA_KEM_TUOI = (By.XPATH, '//div[@id="8"] //h3[text()=\'Trà sữa Kem tươi\']')

    TRA_SUA_TRAN_CHAU_DUONG_DEN_SIZE_M = \
        (By.XPATH, '//div[@id="0"] //h3[text()=\'Trà sữa trân châu đường đen\']')
    INCREASE_TSTCDD_SIZE_M_QUANTITY_BUTTON = \
        (By.XPATH, '//div[contains(@class, "pos__bill-item 0")] //button[contains(text(), "+")]')
    DECREASE_TSTCDD_SIZE_M_QUANTITY_BUTTON = \
        (By.XPATH, '//div[contains(@class, "pos__bill-item 0")] //button[contains(text(), "-")]')

    TRA_SUA_TRAN_CHAU_DUONG_DEN_SIZE_L = \
        (By.XPATH, '//div[@id="1"] //h3[text()=\'Trà sữa trân châu đường đen\']')
    INCREASE_TSTCDD_SIZE_L_QUANTITY_BUTTON = \
        (By.XPATH, '//div[contains(@class, "pos__bill-item 1")] //button[contains(text(), "+")]')
    DECREASE_TSTCDD_SIZE_L_QUANTITY_BUTTON = \
        (By.CSS_SELECTOR, '//div[contains(@class, "pos__bill-item 1")] //button[contains(text(), "-")]')

    TRA_SUA_TRAN_XOAI = (By.XPATH, '//div[@id="3"] //h3[text()=\'Trà sữa trân xoài\']')
    INCREASE_TSTX_QUANTITY_BUTTON = \
        (By.XPATH, '//div[contains(@class, "pos__bill-item 3")] //button[contains(text(), "+")]')
    DECREASE_TSTX_QUANTITY_BUTTON = \
        (By.XPATH, '//div[contains(@class, "pos__bill-item 3")] //button[contains(text(), "-")]')

    SUBMIT_POPUP = (By.ID, "submit_popup")