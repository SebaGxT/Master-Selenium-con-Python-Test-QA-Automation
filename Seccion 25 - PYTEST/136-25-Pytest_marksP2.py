import pytest
from selenium.webdriver import Keys
from Funciones_Globales.funciones import Funciones_Globales as FG

t =.1

def get_Data():
    return [
        ("rodrigo","1234"),
        #("juan","123323"),
        #("pedro","1212523"),
        #("erika","123342"),
        #("carlos","123sdf"),
        ("Admin","admin123")
    ]

@pytest.mark.login
@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user,clave):
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('Entrando al sistema')
    Fun.insertar_texto('xpath',"//input[contains(@name,'username')]",user,t)
    Fun.insertar_texto('xpath',"//input[contains(@type,'password')]",clave,t)
    Fun.Click_elemento('xpath',"//button[@type='submit'][contains(.,'Login')]",t)
    Fun.Tiempo(t)

def teardown_function():
    print('\nSalida del login')
    dri.close()