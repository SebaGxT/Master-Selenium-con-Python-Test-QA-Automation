# Funcion Navegar

from re import T
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
        global T
        T = FG(dri)

    def test(self):
        T.navegar('https://google.com.ar')
        T.Tiempo(2)

    def test2(self):
        T.navegar2('https://twitter.com',2)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()