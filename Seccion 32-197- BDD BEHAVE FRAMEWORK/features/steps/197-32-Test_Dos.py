from behave import *
from Funciones_Globales.funciones import Funciones_Globales as FG

f = 0.8

@given(u'Abriendo el navegador')
def step_impl(context):
    global dri,Fun
    context.dri =  FG.driverCh2()
    Fun = FG(context.dri)
    Fun.navegar("https://demoqa.com/text-box",f)


@when(u'Cargando el nombre del usuario')
def step_impl(context):
    Fun.insertar_texto("xpath","//input[@id='userName']","Sebastian",f)


@then(u'Cargando su email')
def step_impl(context):
    Fun.insertar_texto("xpath","//input[@id='userEmail']","Sebastian@gmail.com",f)


@then(u'Cargando su direccion')
def step_impl(context):
    Fun.insertar_texto("xpath","//textarea[@id='currentAddress']","Nueva dirección",f)
    context.dri.close()