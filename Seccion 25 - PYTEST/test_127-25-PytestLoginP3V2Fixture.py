from Funciones_Globales.funciones import Funciones_Globales as FG

def setup_function(function):
    global dri
    global Fun
    global t
    t = .1
    dri = FG.driverCh2()
    Fun = FG(dri)
    Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',t)

def teardown_function(function):
    dri.quit()

def test_login():
    Fun.insertar_texto('xpath',"//input[@id='Email']","admin@yoursto.com",t)
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin",t)
    Fun.Click_elemento('xpath',"//button[@type='submit']",t)
    e1 = Fun.validar_elemento("xpath","//li[contains(.,'No customer account found')]")
    e1 = e1.text
    if e1 == "No customer account found":
        print("Prueba de validacion usuario exitosa")
    else:
        print("Prueba de validacion usuario incorrecta")
    
def test_login2():
    Fun.insertar_texto('xpath',"//input[@id='Email']"," ",t)
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin",t)
    Fun.Click_elemento('xpath',"//button[@type='submit']",t)
    e1 = Fun.validar_elemento("xpath","//span[@id='Email-error']")
    e1 = e1.text
    if e1 == "Please enter your email":
        print("Prueba de validacion usuario vacio exitosa")
    else:
        print("Prueba de validacion usuario vacio incorrecta")

def test_login3():
    Fun.insertar_texto('xpath',"//input[@id='Email']","ad",t)
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin",t)
    Fun.Click_elemento('xpath',"//button[@type='submit']",t)
    e1 = Fun.validar_elemento("xpath","//span[@id='Email-error']")
    e1 = e1.text
    if e1 == "Wrong email":
        print("Prueba de validacion email exitosa")
    else:
        print("Prueba de validacion email incorrecta")

def test_login4():
    Fun.insertar_texto('xpath',"//input[@id='Email']","admin@yourstore.com",t)
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin",t)
    Fun.Click_elemento('xpath',"//button[@type='submit']",t)
    e1 = Fun.validar_elemento("xpath","//h1[contains(.,'Dashboard')]")
    e1 = e1.text
    if e1 == "Dashboard":
        print("Prueba de ingreso exitosa")
    else:
        print("Prueba de ingreso incorrecta")