# Reto Multiple Seleccion Check Box

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE
from Funciones.funciones import Funciones_Globales as FG

t = 1

class base_test(unittest.TestCase):

    def setUp(self):
        global dri
        dri=FG.driverCh()
        
    def test(self):
        f = FG(dri)
        f.navegar2('https://demo.seleniumeasy.com/basic-checkbox-demo.html',t)
        f.CheckBoxMul_RadioButton_Xpath_Valida("(//input[contains(@type,'checkbox')])",2,5,t)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()