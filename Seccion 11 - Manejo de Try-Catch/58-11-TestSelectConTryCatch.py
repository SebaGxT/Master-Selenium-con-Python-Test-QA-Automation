# Try Catch

import time
from selenium import webdriver as WD
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

t = 0.7

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html')

try:
    diasSelect = WW(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="select-demo"]')))
    dias = Select(diasSelect)

    dias.select_by_visible_text('Sunday')
    time.sleep(t)

    dias.select_by_index(2)
    time.sleep(t)

    dias.select_by_value("Thursday")
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print('El elemento no fue encontrado')

try:
    ciudadSelect = WW(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="multi-select"]')))
    ciudad=Select(ciudadSelect)

    ciudad.select_by_value("California")
    time.sleep(t)
    ciudad.select_by_value("New York")
    time.sleep(t)
    ciudad.select_by_index(2)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print('El elemento no fue encontrado')

driver.quit()
