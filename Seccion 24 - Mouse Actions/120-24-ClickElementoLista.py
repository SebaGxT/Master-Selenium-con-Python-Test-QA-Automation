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
        Fun.navegar("https://google.com.ar/")
        Fun.insertar_texto("xpath","//input[@type='text']","Ferrari")
        Fun.ClickXY_AC(800,480)
        Fun.Tiempo(5)

    def tearDown(self):
        dri.quit()

if __name__ == "__main__":
    unittest.main()