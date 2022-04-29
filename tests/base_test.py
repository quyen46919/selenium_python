import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from tests.test_home_page import TestHomePage
from pages.home_page import HomePage
import webdriver_manager.chrome


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        # driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
        self.driver.get("https://quyen46919.github.io/POSProject/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePage)
    unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main()
