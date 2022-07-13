# Test Links - Verificar cantidad de links en la pagina y hacer click en un link a traves de test link

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
driver.get('https://demo.seleniumeasy.com/input-form-demo.html')


try:

    links = driver.find_elements(By.TAG_NAME,"a")
    print(f'El numero de links en la pagina es: {len(links)}')

    for x in links:
        print(x.text)
    
    driver.find_element(By.LINK_TEXT,'Date pickers').click()
    time.sleep(t)

    driver.find_element(By.LINK_TEXT,'JQuery Date Picker').click()
    time.sleep(t)

except TOE:
    print(TOE.msg)
    print('Hubo un error en la operacion')

time.sleep(t)
driver.quit()