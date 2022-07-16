# Validacion de texto

import time
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://demo.seleniumeasy.com/input-form-demo.html')

t = 2

try:

    btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit'][contains(.,'Send')]")))
    
    if btn is not None:
        driver.execute_script("arguments[0].scrollIntoView();",btn)
        btn = driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Send')]")
        btn.click()

        validname = driver.find_element(By.XPATH,"//small[@class='help-block'][contains(.,'Please supply your first name')]")

        if (validname.is_displayed()==True):
            driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys('Sebastian')
        
        validname = driver.find_element(By.XPATH,"//small[@class='help-block'][contains(.,'Please supply your last name')]")

        if (validname.is_displayed()==True):
            driver.find_element(By.XPATH,"//input[@name='last_name']").send_keys('de la Vega')
        
        time.sleep(t)

        if (btn.is_enabled()==True):
            print('El boton esta habilitado')
        else:
            print('El boton no esta habilitado')

    else:
        print('No se encontro el boton')

except TOE:
    print(TOE.msg)
    print('Hubo un problema en el proceso')

time.sleep(t)
driver.quit()