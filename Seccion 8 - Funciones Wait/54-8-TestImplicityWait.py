# Espera Implicita - Implicity Wait

import time
from selenium import webdriver as WD
from selenium.webdriver.common.by import By


options = WD.ChromeOptions()
options.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=options)

driver.get('https://demoqa.com/text-box')
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@id='userNam']").send_keys('Sebastian')


driver.quit()