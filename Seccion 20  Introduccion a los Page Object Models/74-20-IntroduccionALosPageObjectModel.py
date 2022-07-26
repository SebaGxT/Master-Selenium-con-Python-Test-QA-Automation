# Introduccion a POM

import time
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
        global t
        dri=FG.driverCh()
        t = 2
        dri.get('https://google.com.ar')
        time.sleep(t)

    def test(self):
        f = FG(dri)
        f.saludos()
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()