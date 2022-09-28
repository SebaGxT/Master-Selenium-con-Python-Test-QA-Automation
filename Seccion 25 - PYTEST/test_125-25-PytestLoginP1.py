import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

global dri
global Fun

t = 1

dri = FG.driverCh2()
Fun = FG(dri)

def test_login():
    Fun.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F',t)
    Fun.insertar_texto('xpath',"//input[@id='Email']","admin@yourstore.com",t)
    Fun.insertar_texto('xpath',"//input[@id='Password']","admin",t)
    Fun.Click_elemento('xpath',"//button[@type='submit']",t)
    dri.quit()