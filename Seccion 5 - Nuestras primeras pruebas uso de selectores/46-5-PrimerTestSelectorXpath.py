# Primer test Selector Xpath

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://demoqa.com/text-box')

nom = driver.find_element(By.XPATH,"//input[@id='userName']")
nom.send_keys('Sebastian')

driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys('sebastian@gmail.com')
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys('Direccion Uno')
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys('Direccion Dos')

# Ejecucion de script JS para bajar el scroll de la ventana
driver.execute_script("window.scrollTo(0,200)")

time.sleep(2)

driver.find_element(By.XPATH,"//button[@id='submit']").click()

time.sleep(4)

driver.quit()