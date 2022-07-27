import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

class Funciones_Globales():

    def __init__(self,driver):
        self.driver = driver
    
    def driverCh():
        ops = webdriver.ChromeOptions()
        ops.add_argument('--start-maximized')
        driver=webdriver.Chrome(chrome_options=ops)
        return driver

    def saludos(self):
        print('Bienvenido a Page Object Model')
    
    def Tiempo(self,tiempo):
        t = time.sleep(tiempo)
        return t

    def navegar(self,url):
        self.driver.get(url)
    
    def navegar2(self,url,tiempo):
        self.driver.get(url)
        Funciones_Globales.Tiempo(self,tiempo)