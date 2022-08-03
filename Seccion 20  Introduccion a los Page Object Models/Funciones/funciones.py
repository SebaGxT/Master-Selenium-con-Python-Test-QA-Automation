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
        print(f'Pagina abierta: {url}')
    
    def navegar2(self,url,tiempo):
        self.driver.get(url)
        print(f'Pagina abierta: {url}')
        Funciones_Globales.Tiempo(self,tiempo)

    def texto_Xpath(self,xpath,text,tiempo):
        val = self.driver.find_element(By.XPATH,xpath)
        val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val.clear()
        val.send_keys(text)
        print(f'Escribiendo en el campo {xpath} el texto: {text}')
        Funciones_Globales.Tiempo(self,tiempo)
    
    def texto_ID(self,Id,text,tiempo):
        val = self.driver.find_element(By.ID,Id)
        val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val.clear()
        val.send_keys(text)
        print(f'Escribiendo en el campo {Id} el texto: {text}')
        Funciones_Globales.Tiempo(self,tiempo)

    def texto_Xpath_Valida(self,xpath,text,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.clear()
            val.send_keys(text)
            print(f'Escribiendo en el campo {xpath} el texto: {text}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
    
    def texto_ID_Valida(self,Id,text,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val.clear()
            val.send_keys(text)
            print(f'Escribiendo en el campo {Id} el texto: {text}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)
    
    def Click_Xpath_Valida(self,xpath,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val.click()
            print(f'Se da click en el elemento {xpath}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
    
    def Click_ID_Valida(self,Id,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val.click()
            print(f'Se da click en el elemento {Id}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)
    
    def Select_Lista_Xpath_Valida(self,xpath,op,sel,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.XPATH,xpath)
            val = Select(val)
            op = str.lower(op)
            if op == "text":
                val.select_by_visible_text(sel)
                print(f'Opcion de la lista {xpath} seleccionada por texto: {sel}')
            elif op == "value":
                val.select_by_value(sel)
                print(f'Opcion de la lista {xpath} seleccionada por valor: {sel}')
            elif op == "index":
                val.select_by_index(sel)
                print(f'Opcion de la lista {xpath} seleccionada por indice: {sel}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + xpath)
        
    def Select_Lista_Id_Valida(self,Id,op,sel,tiempo):
        try:
            val = WW(self.driver,5).until(EC.visibility_of_element_located((By.ID,Id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val = self.driver.find_element(By.ID,Id)
            val = Select(val)
            op = str.lower(op)
            if op == "text":
                val.select_by_visible_text(sel)
                print(f'Opcion de la lista {Id} seleccionada por texto: {sel}')
            elif op == "value":
                val.select_by_value(sel)
                print(f'Opcion de la lista {Id} seleccionada por valor: {sel}')
            elif op == "index":
                val.select_by_index(sel)
                print(f'Opcion de la lista {Id} seleccionada por indice: {sel}')
            Funciones_Globales.Tiempo(self,tiempo)
        except TOE as toe:
            print(toe.msg)
            print('No se enconto el elemento' + Id)
