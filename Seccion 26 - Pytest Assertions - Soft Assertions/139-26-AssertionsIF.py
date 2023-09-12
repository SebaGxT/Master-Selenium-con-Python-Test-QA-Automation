import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

@pytest.mark.validarIF
def test_validar_if():
    nom1="Rodrigo"
    nom2="Juan"

    if(nom1==nom2):
        print("El test paso")
    else:
        print("El test no paso")