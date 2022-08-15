# Funcion Upload File

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
        f.navegar2('https://testpages.herokuapp.com/styled/file-upload-test.html',t)
        f.Upload_File_Xpath_Valida("//input[contains(@id,'fileinput')]","C://Users//gueri//Desktop//Programacion y otros//Cursos//Master Selenium con Python Test QA Automation//Seccion 20  Introduccion a los Page Object Models//IMG//demo.jpg",t)
        f.Click_Xpath_Valida("//input[@id='itsanimage']",t)
        f.Click_Xpath_Valida("//input[@type='submit']",t)
        f.Tiempo(3)


    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()