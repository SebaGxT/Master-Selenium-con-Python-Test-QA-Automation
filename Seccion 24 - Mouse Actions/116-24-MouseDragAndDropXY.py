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
        Fun.navegar('http://jqueryui.com/draggable/',t)
        Fun.DragDropXY_AC("xpath","//div[@id='draggable']",150,120,4)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()