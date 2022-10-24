from Funciones_Globales.funciones import Funciones_Globales as FG

global Fun

class funciones_login():

    def __init__(self,driver):
        self.driver = driver
        
    def validacion_cuenta_activa(self,email,password,t=.1):
        Fun = FG(self.driver)
        Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',t)
        Fun.insertar_texto('xpath',"//input[@id='Email']",email,t)
        Fun.insertar_texto('xpath',"//input[@id='Password']",password,t)
        Fun.Click_elemento('xpath',"//button[@type='submit']",t)
        e1 = Fun.validar_elemento("xpath","//li[contains(.,'No customer account found')]")
        e1 = e1.text
        if e1 == "No customer account found":
            print("El Usuario no existe")
        else:
            print("El Usuario existe")

    def validacion_email(self,email,password,t=.1):
        Fun = FG(self.driver)
        Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',t)
        Fun.insertar_texto('xpath',"//input[@id='Email']",email,t)
        Fun.insertar_texto('xpath',"//input[@id='Password']",password,t)
        Fun.Click_elemento('xpath',"//button[@type='submit']",t)
        e1 = Fun.validar_elemento("xpath","//span[@id='Email-error']")
        e1 = e1.text
        if e1 == "Wrong email":
            print("Prueba de validacion email incorrecto exitosa")
        elif e1 == "Please enter your email":
            print("Prueba de validacion email vacio exitosa")
        else:
            print("Prueba de validacion email incorrecta")
    
    def validacion_password_incorrecto(self,email,password,t=.1):
        Fun = FG(self.driver)
        Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',t)
        Fun.insertar_texto('xpath',"//input[@id='Email']",email,t)
        Fun.insertar_texto('xpath',"//input[@id='Password']",password,t)
        Fun.Click_elemento('xpath',"//button[@type='submit']",t)
        e1 = Fun.validar_elemento("xpath","//li[contains(.,'The credentials provided are incorrect')]")
        e1 = e1.text
        if e1 == "The credentials provided are incorrect":
            print("La contraseña es incorrecta")
        else:
            print("La contraseña es correcta")
    
    def login_correcto(self,email,password,t=.1):
        Fun = FG(self.driver)
        Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',t)
        Fun.insertar_texto('xpath',"//input[@id='Email']",email,t)
        Fun.insertar_texto('xpath',"//input[@id='Password']",password,t)
        Fun.Click_elemento('xpath',"//button[@type='submit']",t)
        e1 = Fun.validar_elemento("xpath","//h1[contains(.,'Dashboard')]")
        e1 = e1.text
        if e1 == "Dashboard":
            print("Prueba de ingreso exitosa")
        else:
            print("Prueba de ingreso incorrecta")
    