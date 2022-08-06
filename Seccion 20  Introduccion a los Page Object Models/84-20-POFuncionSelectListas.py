# Funcion Select Listas

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
        f.navegar2('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html',t)
        f.Select_Lista_Id_Valida('select-demo','value','Sunday',t)
        f.Tiempo(3)
        f.Select_Lista_Id_Valida('select-demo','text','Tuesday',t)
        f.Tiempo(3)
        f.Select_Lista_Id_Valida('select-demo','index','6',t)
        f.Tiempo(3)
        f.Select_Lista_Id_Valida('select-demo','valu','Sunday',t)
        f.Select_Lista_Id_Valida('select-demo','tex','Tuesday',t)
        f.Select_Lista_Id_Valida('select-demo','inde','6',t)
    
    def test2(self):
        f = FG(dri)
        f.navegar2('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html',t)
        f.Select_Lista_Xpath_Valida("//select[contains(@id,'select-demo')]",'value','Sunday',t)
        f.Tiempo(3)
        f.Select_Lista_Xpath_Valida("//select[contains(@id,'select-demo')]",'text','Tuesday',t)
        f.Tiempo(3)
        f.Select_Lista_Xpath_Valida("//select[contains(@id,'select-demo')]",'index','6',t)
        f.Tiempo(3)
        f.Select_Lista_Xpath_Valida("//select[contains(@id,'select-demo')]",'valu','Sunday',t)
        f.Select_Lista_Xpath_Valida("//select[contains(@id,'select-demo')]",'tex','Tuesday',t)
        f.Select_Lista_Xpath_Valida("//select[contains(@id,'select-demo')]",'inde','6',t)

    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()