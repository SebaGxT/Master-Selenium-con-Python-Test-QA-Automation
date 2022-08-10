# Mejora de funciones

import unittest
from Funciones.funciones import Funciones_Globales as FG

class base_test(unittest.TestCase):

    def setUp(self):
        global dri
        dri=FG.driverCh()
        global Fun
        Fun = FG(dri)

    def test(self):
        Fun.navegar2('https://saucedemo.com',2)
        Fun.texto_Mixto_Valida('xpath',"//input[@id='user-name']","standard_user",2)
        Fun.texto_Mixto_Valida('id',"password","secret_sauce",2)
        
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()