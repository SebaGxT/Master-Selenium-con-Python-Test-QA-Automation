# Excel openpyxl

import unittest
from Funciones.funciones import Funciones_Globales as FG
from Funciones.funciones_excel import Funexcel as FE

t = 2

class CompletarDatosExcel(unittest.TestCase):

    def setUp(self):
        global dri
        dri=FG.driverFi()
        global drifg
        drifg = FG(dri)
        global funex
        funex = FE(dri)

    def test(self):
        drifg.navegar('https://demoqa.com/text-box',t)
        
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()