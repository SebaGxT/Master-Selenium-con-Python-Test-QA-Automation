# Mejorando la Funcion Texto con Xpath

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
        global Fun
        Fun = FG(dri)

    def test(self):
        Fun.navegar2('https://saucedemo.com',t)
        Fun.texto_Xpath_Valida("//input[@id='user-name']","standard_user",t)
        Fun.texto_Xpath_Valida("//input[@id='password']","secret_sauce",t)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()