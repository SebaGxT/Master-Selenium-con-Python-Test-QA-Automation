from Funciones_Globales.funciones import Funciones_Globales as FG
from Funciones_Globales.funciones_Login import funciones_login as FL

global dri

def test_login():
    dri = FG.driverCh2()
    Fl = FL(dri)
    Fl.validacion_cuenta_activa("admin@yoursto.com","admin")
    Fl.validacion_email(" ","admin")
    Fl.validacion_email("ed","admin")
    Fl.validacion_password_incorrecto("admin@yourstore.com","adm")
    Fl.login_correcto("admin@yourstore.com","admin")
    dri.quit()
