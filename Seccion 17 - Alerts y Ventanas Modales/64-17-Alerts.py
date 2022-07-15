# Alertas

import time
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TOE

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://demo.seleniumeasy.com/bootstrap-modal-demo.html')

t = 3

try:

    driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()
    try:
        btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]")))
        btn = driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]").click()
        time.sleep(t)
    except TOE:
        print(TOE.msg)
        print('No se encontro el elemento')
    driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()
    try:
        btn = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,"(//a[@href='#'][contains(.,'Close')])[1]")))
        btn = driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Close')])[1]").click()
        time.sleep(t)
    except TOE:
        print(TOE.msg)
        print('No se encontro el elemento')
#driver.switch_to.alert.accept() presiona el boton aceptar en una alerta
#driver.switch_to.alert.dismiss() presiona el boton cancelar en una alerta

except TOE:
    print(TOE.msg)
    print('Hubo un error en el proceso')

time.sleep(t)
driver.quit()