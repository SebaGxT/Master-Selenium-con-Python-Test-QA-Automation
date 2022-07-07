# Manejo de combo box y list box

from re import T
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

t=.7
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html')

opt = WW(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//select[@id='select-demo']")))
dias = driver.find_element(By.XPATH,"//select[@id='select-demo']")
SelectorDeDias = Select(dias) # Crea el objeto seleccionador con la direccion del elemento que se pasa por variable como parametro
SelectorDeDias.select_by_visible_text("Sunday") # Se debe respetar Mayusculas y minusculas
time.sleep(t)
SelectorDeDias.select_by_index(3)
time.sleep(t)
SelectorDeDias.select_by_value("Saturday")
time.sleep(t)

ciudad = Select(driver.find_element(By.ID,"multi-select"))

ciudad.select_by_index(1)
time.sleep(t)
ciudad.select_by_index(3)
time.sleep(t)
ciudad.select_by_index(6)
time.sleep(t)

driver.quit()