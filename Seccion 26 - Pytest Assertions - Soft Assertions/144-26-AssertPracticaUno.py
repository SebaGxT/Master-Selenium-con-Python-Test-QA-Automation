import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

t=.8

@pytest.fixture(scope='module')
def setup_login():
    global dri,Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    dri.implicitly_wait(20)
    print('Entrando al sistema')
    Fun.insertar_texto("xpath","//input[@name='username']","Admin",t)
    Fun.insertar_texto("xpath","//input[@name='password']","admin123",t)
    Fun.Click_elemento("xpath","//button[@type='submit']",t)

def teardown_function():
    print('\nFin de los test')
    dri.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno():
    etiqueta = Fun.validar_elemento_localizado("xpath","//h6[contains(.,'Dashboard')]").text
    print(etiqueta)
    if(etiqueta=="Dashboard"):
        print("\n##############")
        print("Estas en la pagina de inicio")
        print("##############\n")
        assert etiqueta=="Dashboard"
    else:
        assert etiqueta=="Dashboard","No pudiste entrar al sistema"

@pytest.mark.loginfail
@pytest.mark.usefixtures("setup_login")
def test_dos():
    etiqueta = Fun.validar_elemento_localizado("xpath","//h6[contains(.,'Dashboard')]").text
    print(etiqueta)
    if(etiqueta=="Dashboart"):
        print("\n##############")
        print("Estas en la pagina de inicio")
        print("##############\n")
        assert etiqueta=="Dashboard"
    else:
        assert etiqueta=="Dashboart","No pudiste entrar al sistema"