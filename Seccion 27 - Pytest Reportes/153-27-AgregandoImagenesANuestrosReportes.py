import pytest
import allure
from Funciones_Globales.funciones import Funciones_Globales as FG
from allure_commons.types import AttachmentType

t = 1

@pytest.fixture(scope='module')
def setup_login_uno():
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    print('Entrando al sistema')
    Fun.insertar_texto('id','Email','admin@yourstore.com',t)
    Fun.insertar_texto('id','Password','admin',t)
    Fun.Click_elemento('xpath',"//button[@type='submit'][contains(.,'Log in')]",t)
    Fun.Tiempo(t) 

@pytest.fixture(scope='module')
def setup_login_dos():
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    print('Entrando al sistema')
    Fun.insertar_texto('xpath',"//input[contains(@name,'username')]",'Admin',t)
    Fun.insertar_texto('xpath',"//input[contains(@type,'password')]",'admin123',t)
    allure.attach(dri.get_screenshot_as_png(),name="login",attachment_type=AttachmentType.PNG)
    Fun.Click_elemento('xpath',"//button[@type='submit'][contains(.,'Login')]",t)
    allure.attach(dri.get_screenshot_as_png(),name="botonlogin",attachment_type=AttachmentType.PNG)
    Fun.Tiempo(t)

@pytest.mark.usefixtures('setup_login_uno')
def test_login_uno():
    Fun.Click_elemento('xpath',"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a",t)
    Fun.Click_elemento('xpath',"/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a",t)
    allure.attach(dri.get_screenshot_as_png(),name="customersbefore",attachment_type=AttachmentType.PNG)
    Fun.Click_elemento('xpath',"/html/body/div[3]/div[1]/form[1]/div/div/a",t)
    Fun.insertar_texto('xpath','//*[@id="Email"]',"aasd@gmail.com",t)
    Fun.insertar_texto('xpath','//*[@id="Password"]',"Pass",t)
    Fun.insertar_texto('xpath','//*[@id="FirstName"]',"AAa",t)
    Fun.insertar_texto('xpath','//*[@id="LastName"]',"AaA",t)
    Fun.CheckBox_RadioButton('xpath','//*[@id="Gender_Male"]',t)
    Fun.Click_elemento('xpath','//*[@id="customer-info"]/div[2]/div[6]/div[2]/span[1]/span/span',t)
    Fun.Click_elemento('xpath',"//a[@data-value='2023/8/6']",t)
    Fun.insertar_texto('xpath',"//input[@id='Company']","bbb",t)
    allure.attach(dri.get_screenshot_as_png(),name="customers",attachment_type=AttachmentType.PNG)
    Fun.Click_elemento('xpath',"//button[@name='save']",t)
    allure.attach(dri.get_screenshot_as_png(),name="customerssave",attachment_type=AttachmentType.PNG)
    Fun.validar_elemento_visible('xpath',"//div[contains(@class,'alert alert-success alert-dismissable')]",t)

@pytest.mark.usefixtures('setup_login_dos')
def test_login_dos():
    Fun.Click_elemento('xpath',"//a[@href='/web/index.php/admin/viewAdminModule']",t)
    Fun.Click_elemento('xpath',"(//span[contains(.,'User Management')])[2]",t)
    Fun.Click_elemento('xpath',"//a[contains(.,'Users')]",t)
    allure.attach(dri.get_screenshot_as_png(),name="users",attachment_type=AttachmentType.PNG)
    Fun.insertar_texto('xpath',"//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]","Cassidy.Hope",t)


def teardown_function():
    print('\nFin de los test')
    dri.close()