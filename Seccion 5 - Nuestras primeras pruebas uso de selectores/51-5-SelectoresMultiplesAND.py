# Multiples selectores

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://demoqa.com/text-box')
time.sleep(2)


nom = driver.find_element(By.XPATH,"//input[@type='text' and @id='userName']") 
nom.send_keys('Sebastian')        
driver.find_element(By.CSS_SELECTOR,'#userEmail').send_keys('Sebastian@email.com')
driver.find_element(By.CSS_SELECTOR,'#currentAddress').send_keys('Direccion Uno')
driver.find_element(By.CSS_SELECTOR,'#permanentAddress').send_keys('Direccion Dos')
driver.execute_script('window.scrollTo(0,200)')
driver.find_element(By.CSS_SELECTOR,'#submit').click()

time.sleep(4)

driver.quit()