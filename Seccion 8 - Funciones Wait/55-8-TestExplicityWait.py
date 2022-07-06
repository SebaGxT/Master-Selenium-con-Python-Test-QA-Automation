# Espera Explicita - Explicity wait

import time as T
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC

options = WD.ChromeOptions()
options.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=options)

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

btn = WW(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="#"][contains(.,"No, thanks!")]')))
btn.click()


driver.find_element(By.XPATH,'//*[@id="user-message"]').send_keys('Hola' + Keys.TAB + Keys.ENTER)

T.sleep(1)

driver.find_element(By.XPATH,'//*[@id="sum1"]').send_keys('5'+Keys.TAB+'5'+Keys.TAB+Keys.ENTER)

T.sleep(2)

driver.quit()