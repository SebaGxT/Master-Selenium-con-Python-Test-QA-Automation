# Navegacion web back - forward

import time as T
from selenium import webdriver
from selenium.webdriver.common.by import By

t = 4 # Funcion Back() puede llegar a fallar con tiempos de 4 o superior

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://demoqa.com/text-box')
T.sleep(t)

driver.get('https://www.selenium.dev/documentation/webdriver/elements/')
T.sleep(t)

driver.get('https://www.google.com.ar')
T.sleep(t)

driver.execute_script('window.history.go(-1)') # Script de JS para moverse atras o adelante en el historial

driver.back()

driver.forward()

T.sleep(t)

driver.quit()