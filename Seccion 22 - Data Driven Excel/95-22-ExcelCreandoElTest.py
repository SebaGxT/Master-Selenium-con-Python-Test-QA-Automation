# Excel openpyxl

import unittest
from Funciones.funciones import Funciones_Globales as FG
from Funciones.funciones_excel import Funexcel as FE

t = .3

class CompletarDatosExcel(unittest.TestCase):

    def setUp(self):
        global dri
        global drifg
        global funex
        global ruta
        global hoja
        dri=FG.driverCh()
        drifg = FG(dri)
        funex = FE(dri)
        ruta = "C://Users//gueri//Desktop//Programacion y otros//Cursos//Master Selenium con Python Test QA Automation//Seccion 22 - Data Driven Excel//datos.xlsx"
        hoja = "Hoja1"

    def test(self):
        drifg.navegar('https://demoqa.com/text-box',t)
        filas = funex.obtener_Cant_Filas(ruta,hoja)
        tipo = "xpath"
        for r in range(2,filas+1):
            nombre = funex.lectura_Datos(ruta,hoja,r,1)
            email = funex.lectura_Datos(ruta,hoja,r,2)
            dir1 = funex.lectura_Datos(ruta,hoja,r,3)
            dir2 = funex.lectura_Datos(ruta,hoja,r,4)
            drifg.insertar_texto(tipo,"//input[@id='userName']",nombre,t)
            drifg.insertar_texto(tipo,"//input[@id='userEmail']",email,t)
            drifg.insertar_texto(tipo,"//textarea[@id='currentAddress']",dir1,t)
            drifg.insertar_texto(tipo,"//textarea[@id='permanentAddress']",dir2,t)
            drifg.Click_elemeto(tipo,"//button[@id='submit']",t)
            if (drifg.validar_elemento_visible("xpath","//p[@id='name']",t)):
                funex.escritura_Datos(ruta,hoja,r,5,"Insertado OK")
            else:
                funex.escritura_Datos(ruta,hoja,r,5,"Error al insertar")
              
    def tearDown(self):
        dri.quit()

if __name__ == '__main__':
    unittest.main()