# Plantilla de unittest

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

class base_test(unittest.TestCase):

    def setUp(self):
        
        global driver
        global t
        t = 2
        ops = webdriver.ChromeOptions()
        ops.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=ops)
        driver.get('')
        time.sleep(t)

    def test(self):
        pass
        
    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()