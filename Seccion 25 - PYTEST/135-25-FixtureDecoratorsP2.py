import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

# @pytest.fixture(scope='module')
# def setup_login_uno():
#     global dri
#     global Fun
#     dri = FG.driverCh2()
#     Fun = FG(dri)
#     Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
#     print('Entrando al sistema')
#     Fun.insertar_texto('id','Email','admin@yourstore.com',2)
#     Fun.insertar_texto('id','Password','admin',2)
#     Fun.Click_elemento('xpath',"//button[@type='submit'][contains(.,'Log in')]",2)
#     Fun.Tiempo(2) 
#     yield
#     dri.quit()
#     print('\nSalida del login uno')

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

# @pytest.mark.usefixtures('setup_login_uno')
# def test_login_uno():
#     Fun.Click_elemento('xpath',"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a",2)
#     Fun.Click_elemento('xpath',"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a",2)
#     Fun.Click_elemento('xpath',"/html/body/div[3]/div[1]/form[1]/div/div/a",2)
#     Fun.insertar_texto('xpath','//*[@id="Email"]',"a@gmail.com",2)
#     Fun.insertar_texto('xpath','//*[@id="Password"]',"Pass",2)
#     Fun.insertar_texto('xpath','//*[@id="FirstName"]',"AAa",2)
#     Fun.insertar_texto('xpath','//*[@id="LastName"]',"AaA",2)
#     Fun.CheckBox_RadioButton('xpath','//*[@id="Gender_Male"]',2)
#     Fun.Click_elemento('xpath','//*[@id="customer-info"]/div[2]/div[6]/div[2]/span[1]/span/span',2)

@pytest.mark.usefixtures('setup_login_dos')
def test_login_dos():
    Fun.Click_elemento('xpath',"//a[@href='/web/index.php/admin/viewAdminModule']",2)
    Fun.Click_elemento('xpath',"(//span[contains(.,'User Management')])[2]",2)
    Fun.Click_elemento('xpath',"//a[contains(.,'Users')]",2)
    Fun.insertar_texto('xpath','//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input',"Admin",2)
    