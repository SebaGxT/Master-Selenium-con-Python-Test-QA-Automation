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
        Fun.navegar('https://testpages.herokuapp.com/styled/drag-drop-javascript.html',t)
        Fun.DragDrop_AC("xpath","(//p[contains(.,'Drag me')])[1]","//div[@id='droppable1']",t)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()