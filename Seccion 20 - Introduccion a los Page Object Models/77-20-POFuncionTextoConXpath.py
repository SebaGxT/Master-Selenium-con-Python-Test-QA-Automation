# Funcion Texto con Xpath

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE
from Funciones.funciones import Funciones_Globales as FG

class base_test(unittest.TestCase):

    def setUp(self):
        global dri
        dri=FG.driverCh()
        global Fun
        Fun = FG(dri)

    def test(self):
        Fun.navegar2('https://saucedemo.com',2)
        Fun.texto_Xpath("//input[@id='user-name']","standard_user",2)
        Fun.texto_Xpath("//input[@id='password']","secret_sauce",2)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()