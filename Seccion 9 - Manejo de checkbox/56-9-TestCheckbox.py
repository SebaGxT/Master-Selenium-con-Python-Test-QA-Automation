# Manejo de check box

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')

ckbx = WW(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='isAgeSelected']")))
ckbx.click()

ckbx2 = WW(driver,10).until(EC.presence_of_element_located((By.XPATH,"(//input[@type='checkbox'])[2]")))
ckbx2.click()
ckbx3 = WW(driver,10).until(EC.presence_of_element_located((By.XPATH,"(//input[@type='checkbox'])[3]")))
ckbx3.click()

driver.execute_script('window.scrollTo(0,200)')

time.sleep(3)
driver.quit()