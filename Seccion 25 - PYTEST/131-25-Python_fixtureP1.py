from Funciones_Globales.funciones import Funciones_Globales as FG


def setup_function(function):
    global dri
    global Fun
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

def teardown_function(function):
    dri.quit()

def test_login():
    Fun.insertar_texto('xpath',"//input[@id='Email']","admin@yoursto.com")
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin")
    Fun.Click_elemento('xpath',"//button[@type='submit']")
    e1 = Fun.validar_elemento("xpath","//li[contains(.,'No customer account found')]")
    e1 = e1.text
    if e1 == "No customer account found":
        print("Prueba de validacion usuario exitosa")
    else:
        print("Prueba de validacion usuario incorrecta")

def test_login2():
    Fun.insertar_texto('xpath',"//input[@id='Email']","admin@yourstore.com")
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin")
    Fun.Click_elemento('xpath',"//button[@type='submit']")
    Fun.Click_elemento('xpath',"(//p[contains(.,'Catalog')])[1]")
    Fun.Click_elemento('xpath',"(//p[contains(.,'Products')])[1]")
    Fun.insertar_texto('xpath',"//input[@id='SearchProductName']",'Computer')
    Fun.Click_elemento('xpath',"//button[@id='search-products']")
    Fun.Tiempo(3)