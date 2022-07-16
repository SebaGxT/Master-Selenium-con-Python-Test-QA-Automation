# Condicionales validacion con IF

import time
from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait as WW
from selenium.common.exceptions import TimeoutException as TOE

ops = WD.ChromeOptions()
ops.add_argument('--start-maximized')
driver = WD.Chrome(chrome_options=ops)
driver.get('https://demoqa.com/text-box')

t = 3

'''
driver.get('https://demoqa.com')

validacion de existencia de un elemento

titulo = driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")

print(titulo.is_enabled())

btn = driver.find_element(By.XPATH,"(//div[contains(@class,'card-up')])[1]")

if (titulo.is_displayed()==True):
    print('Existe la imagen')
    btn.click()
else:
    print('No Existe la imagen')
'''

# Verificar si un boton esta activo
btn = driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")
print(btn.is_enabled())

if (btn.is_enabled==True):
    print('Puedes dar click')
else:
    print('No puedes dar click')

time.sleep(t)
driver.quit()