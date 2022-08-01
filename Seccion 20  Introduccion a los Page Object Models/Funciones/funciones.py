import time
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

    def texto_Xpath(self,xpath,text,tiempo):
        val = self.driver.find_element(By.XPATH,xpath)
        val.clear()
        val.send_keys(text)
        Funciones_Globales.Tiempo(self,tiempo)
    
    def texto_ID(self,Id,text,tiempo):
        val = self.driver.find_element(By.ID,Id)
        val.clear()
        val.send_keys(text)
        Funciones_Globales.Tiempo(self,tiempo)

    def texto_Xpath_Valida(self,xpath,text,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.find_element(By.XPATH,xpath)
            val.clear()
            val.send_keys(text)
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)