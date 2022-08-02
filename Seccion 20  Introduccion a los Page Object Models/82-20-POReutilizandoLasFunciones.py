# Page Login Reutilizando Funciones

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE
from Funciones.funciones import Funciones_Globales as FG
from Funciones.Page_Login import Page_Login as PL

t = 1

class base_test(unittest.TestCase):

    def setUp(self):
        global dri
        dri=FG.driverCh()
        

    def test(self):
        page = PL(dri)
        page.Login_Master("https://www.saucedemo.com/","//input[contains(@id,'user-name')]","standard_user","//input[contains(@id,'password')]","secret_sauce","//input[contains(@id,'login-button')]",t)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()