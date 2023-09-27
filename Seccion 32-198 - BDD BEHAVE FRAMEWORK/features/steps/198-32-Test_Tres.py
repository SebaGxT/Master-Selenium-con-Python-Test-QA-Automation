from behave import *
from Funciones_Globales.funciones import Funciones_Globales as FG

f = 0.8

@given(u'Abriendo el navegador')
def step_impl(context):
    global dri,Fun
    context.dri =  FG.driverCh2()
    Fun = FG(context.dri)
    Fun.navegar("https://demoqa.com/text-box",f)


@when(u'Cargando el nombre del "{user}"')
def step_impl(context,user):
    Fun.insertar_texto("xpath","//input[@id='userName']",user,f)


@then(u'Cargando su "{email}"')
def step_impl(context,email):
    Fun.insertar_texto("xpath","//input[@id='userEmail']",email,f)


@then(u'Cargando la "{direccion}"')
def step_impl(context,direccion):
    Fun.insertar_texto("xpath","//textarea[@id='currentAddress']",direccion,f)
    context.dri.close()