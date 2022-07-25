# Reto Login

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

class base_test(unittest.TestCase):

    def setUp(self):
        
        global driver
        global t
        t = .7
        ops = webdriver.ChromeOptions()
        ops.add_argument('--start-maximized')
        driver = webdriver.Chrome(chrome_options=ops)
        driver.get('https://www.saucedemo.com/')
        time.sleep(t)

    '''

    Validar login

    Username y pass invalidos - validar texto de error
    Username y pass con numeros - validar mismo texto
    Username vacio
    pass vacio
    ambos vacios
    login valido

    '''

    def testLogin_UserPassInv(self):
        
        try:

            username = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']")))
            passw = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']")))
            btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))

            username = driver.find_element(By.XPATH,"//input[@id='user-name']")
            passw = driver.find_element(By.XPATH,"//input[@id='password']")
            btn = driver.find_element(By.XPATH,"//input[@id='login-button']")

            username.send_keys('asdf')
            passw.send_keys('fdsa')
            time.sleep(t)
            btn.click()

            mensg = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//h3[contains(.,'Epic sadface: Username and password do not match any user in this service')]")))
            mensg = driver.find_element(By.XPATH,"//h3[contains(.,'Epic sadface: Username and password do not match any user in this service')]")
            time.sleep(t)
            if mensg.is_displayed:
                print("Se visualiza el error correctamente")
            else:
                print("No se mostro el error")

        except TOE:
            print(TOE.msg)
            print('Hubo un error al encontrar un elemento')

    def testLogin_UserPassInvNum(self):
        
        try:

            username = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']")))
            passw = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']")))
            btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))

            username = driver.find_element(By.XPATH,"//input[@id='user-name']")
            passw = driver.find_element(By.XPATH,"//input[@id='password']")
            btn = driver.find_element(By.XPATH,"//input[@id='login-button']")

            username.send_keys('asdf1234')
            passw.send_keys('fdsa11234')
            time.sleep(t)
            btn.click()

            mensg = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//h3[contains(.,'Epic sadface: Username and password do not match any user in this service')]")))
            mensg = driver.find_element(By.XPATH,"//h3[contains(.,'Epic sadface: Username and password do not match any user in this service')]")
            time.sleep(t)
            if mensg.is_displayed:
                print("Se visualiza el error correctamente")
            else:
                print("No se mostro el error")

        except TOE:
            print(TOE.msg)
            print('Hubo un error al encontrar un elemento')

    def testLogin_UserVac(self):
        
        try:

            passw = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']")))
            btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))

            passw = driver.find_element(By.XPATH,"//input[@id='password']")
            btn = driver.find_element(By.XPATH,"//input[@id='login-button']")
            
            passw.send_keys('secret_sauce')
            time.sleep(t)
            btn.click()

            mensg = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")))
            mensg = driver.find_element(By.XPATH,"//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
            time.sleep(t)
            if mensg.is_displayed:
                print("Se visualiza el error correctamente")
            else:
                print("No se mostro el error")
        
        except TOE:
            print(TOE.msg)
            print('Hubo un error al encontrar un elemento')

    def testLogin_PassVac(self):
        
        try:

            username = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']")))
            btn = WW(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))

            username = driver.find_element(By.XPATH,"//input[@id='user-name']")
            btn = driver.find_element(By.XPATH,"//input[@id='login-button']")

            username.send_keys('standard_user')
            time.sleep(t)
            btn.click()

            mensg = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='error-message-container error'][contains(.,'Epic sadface: Password is required')]")))
            mensg = driver.find_element(By.XPATH,"//div[@class='error-message-container error'][contains(.,'Epic sadface: Password is required')]")
            time.sleep(t)
            if mensg.is_displayed:
                print("Se visualiza el error correctamente")
            else:
                print("No se mostro el error")

        except TOE:
            print(TOE.msg)
            print('Hubo un error al encontrar un elemento')

    def testLogin_UserPassVac(self):
        
        try:

            btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))

            btn = driver.find_element(By.XPATH,"//input[@id='login-button']")

            btn.click()

            mensg = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")))
            mensg = driver.find_element(By.XPATH,"//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
            time.sleep(t)
            if mensg.is_displayed:
                print("Se visualiza el error correctamente")
            else:
                print("No se mostro el error")
        
        except TOE:
            print(TOE.msg)
            print('Hubo un error al encontrar un elemento')

    def testLogin_Valido(self):
        
        try:

            username = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='user-name']")))
            passw = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']")))
            btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']")))

            username = driver.find_element(By.XPATH,"//input[@id='user-name']")
            passw = driver.find_element(By.XPATH,"//input[@id='password']")
            btn = driver.find_element(By.XPATH,"//input[@id='login-button']")

            username.send_keys('standard_user')
            passw.send_keys('secret_sauce')
            time.sleep(t)
            btn.click()

            titulo = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title'][contains(.,'Products')]")))
            titulo = driver.find_element(By.XPATH,"//span[@class='title'][contains(.,'Products')]")
            time.sleep(t)
            if titulo.is_displayed:
                print('El login fue exitoso')
            else:
                print('Hubo un error en el login')

        except TOE:
            print(TOE.msg)
            print('Hubo un error al encontrar un elemento')

    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()