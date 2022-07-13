# Scroll sobre elemento

import time
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

t = 3

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://pixabay.com/es/')

try:
    buscar = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/es/images/search/?order=ec']")))
    buscar = driver.find_element(By.XPATH,"//a[@href='/es/images/search/?order=ec']")
    ir = driver.execute_script("arguments[0].scrollIntoView();",buscar)
    time.sleep(t)

except TOE:
    print(TOE.msg)
    print('El elemento no esta disponible')

time.sleep(t)
driver.quit()