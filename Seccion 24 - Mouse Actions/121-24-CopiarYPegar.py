import unittest
from Funciones_Globales.funciones import Funciones_Globales as FG

t = 1

class mouse_test(unittest.TestCase):

    def setUp(self):
        global dri
        global Fun
        dri = FG.driverCh()
        Fun = FG(dri)
    
    def test(self):
        Fun.navegar("https://demoqa.com/automation-practice-form")
        Fun.insertar_texto("xpath","//input[contains(@id,'firstName')]","Ferrari")
        Fun.copiar_pegar("xpath","//input[contains(@id,'firstName')]","//input[@id='lastName']",5)
        

    def tearDown(self):
        dri.quit()

if __name__ == "__main__":
    unittest.main()