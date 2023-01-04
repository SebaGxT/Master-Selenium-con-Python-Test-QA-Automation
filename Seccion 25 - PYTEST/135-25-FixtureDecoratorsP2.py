import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

@pytest.fixture(scope='module')
def setup_login_uno():
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    print('Entrando al sistema')
    Fun.insertar_texto('id','Email','admin@yourstore.com',2)
    Fun.insertar_texto('id','Password','admin',2)
    Fun.Click_elemento('xpath',"//button[@type='submit'][contains(.,'Log in')]",2)
    Fun.Tiempo(2) 
    yield
    dri.quit()
    print('\nSalida del login uno')

@pytest.fixture(scope='module')
def setup_login_dos():
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('Entrando al sistema')
    Fun.insertar_texto('xpath',"//input[contains(@name,'username')]",'Admin',2)
    Fun.insertar_texto('xpath',"//input[contains(@type,'password')]",'admin123',2)
    Fun.Click_elemento('xpath',"//button[@type='submit'][contains(.,'Login')]",2)
    Fun.Tiempo(2)
    yield
    dri.quit()
    print('\nSalida del login dos')

@pytest.mark.usefixtures('setup_login_uno')
def test_login_uno():
    pass  

@pytest.mark.usefixtures('setup_login_dos')
def test_login_dos():
    pass