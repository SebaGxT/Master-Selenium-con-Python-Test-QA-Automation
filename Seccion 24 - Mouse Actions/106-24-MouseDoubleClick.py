import unittest
from Funciones_Globales.funciones import Funciones_Globales as FG

t = 1

class mouse_test(unittest.TestCase):

    def setUp(self) :
        global dri
        global Fun
        dri = FG.driverCh()
        Fun = FG(dri)
    
    def test(self):
        Fun.navegar('https://demoqa.com/buttons',t)
        Fun.doble_click_AC("xpath","//button[@id='doubleClickBtn']",t)
        Fun.click_derecho_AC("id","rightClickBtn",t)
        Fun.click_AC("xpath","/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/button[1]",t)
        Fun.Tiempo(4)


    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()
