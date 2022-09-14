from argparse import Action
import unittest
from Funciones_Globales.funciones import Funciones_Globales as FG
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.by import By

t = 1

class base_test(unittest.TestCase):

    def setUp(self):
        global dri
        global Fun
        dri = FG.driverCh()
        Fun = FG(dri)
    
    def test(self):
        Fun.navegar('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login',t)
        Fun.insertar_texto("xpath","//input[@name='username']","Admin",t)
        Fun.insertar_texto("xpath","//input[@type='password']","admin123",t)
        Fun.Click_elemento("xpath","//button[@type='submit']",t)
        admin = dri.find_element(By.XPATH,"//a[contains(.,'Admin')]")
        act = AC(dri)
        act.move_to_element(admin).click(admin).perform()
        sub1 = dri.find_element(By.XPATH,"(//i[contains(@class,'oxd-icon bi-chevron-down')])[1]")
        act.move_to_element(sub1).click(sub1).perform()
        sub2 = dri.find_element(By.XPATH,"(//li[contains(.,'Users')])[2]")
        act.move_to_element(sub2).click(sub2).perform()        

    def tearDown(self):
        dri.quit()
    
if __name__ == '__main__':
    unittest.main()
