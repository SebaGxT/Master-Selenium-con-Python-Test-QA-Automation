# Subir Archivos

import time
from selenium import webdriver as WD
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

t = 2

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://testpages.herokuapp.com/styled/file-upload-test.html')

try:

    btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="fileinput"]')))
    btn = driver.find_element(By.XPATH,'//*[@id="fileinput"]').send_keys("C://Users//gueri//Desktop//Programacion y otros//Cursos//Master Selenium con Python Test QA Automation//Seccion 12 - Upload Files//IMG//demo.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH,'//*[@id="itsanimage"]').click()
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print('El elemento no fue encontrado')

driver.quit()