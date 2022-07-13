# Primer Reto

import time
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE
from selenium.webdriver.support.ui import Select

t = 3

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://demo.seleniumeasy.com/input-form-demo.html')

elemento = ["//input[@name='first_name']","//input[@name='last_name']","//input[@name='email']","//input[@name='phone']","//input[@name='address']",
"//input[@name='city']","//select[@name='state']","//input[@name='zip']","//input[@name='website']",
"//input[@value='no']","//textarea[@name='comment']","//button[@type='submit'][contains(.,'Send')]"]

try:

    for x in elemento:
        buscar = WW(driver,5).until(EC.visibility_of_element_located((By.XPATH,x)))
    
    try:

        nombre= driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys("Sebastian")
        apellido = driver.find_element(By.XPATH,"//input[@name='last_name']").send_keys("de la vega")
        email = driver.find_element(By.XPATH,"//input[@name='email']").send_keys("Sebastiandelavega@mail.com")
        tel = driver.find_element(By.XPATH,"//input[@name='phone']").send_keys("1111111111")
        dire = driver.find_element(By.XPATH,"//input[@name='address']").send_keys('Calle Falsa 123')
        ciudad = driver.find_element(By.XPATH,"//input[@name='city']").send_keys('BSAS')
        estado = Select(driver.find_element(By.XPATH,"//select[@name='state']"))
        estado.select_by_index(5)
        cp = driver.find_element(By.XPATH,"//input[@name='zip']").send_keys("1037")
        webdom = driver.find_element(By.XPATH,"//input[@name='website']").send_keys("google")
        host = driver.find_element(By.XPATH,"//input[@value='no']").click()
        comm = driver.find_element(By.XPATH,"//textarea[@name='comment']").send_keys("Sin Comentarios")
        driver.execute_script("window.scrollTo(0,200)")
        time.sleep(t)
        btn = driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Send')]").click()

    except TOE:
        print(TOE.msg)
        print('Hubo un error en el proceso de completado')

except TOE:
    print(TOE.msg)
    print('Un elemento no fue encontrado')

time.sleep(t)
driver.quit()