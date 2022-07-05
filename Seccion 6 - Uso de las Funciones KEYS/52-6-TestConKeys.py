
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://demoqa.com/text-box')
time.sleep(2)

nom = driver.find_element(By.XPATH,'//input[@id="userName"]')
nom.send_keys('Sebastian' + Keys.TAB + 'Sebastian@mail.com' + Keys.TAB + 'Direccion Uno' + Keys.TAB + 'Direccion Dos' + Keys.TAB + Keys.ENTER)

driver.execute_script('window.scrollTo(0,200)')


time.sleep(4)


driver.quit()