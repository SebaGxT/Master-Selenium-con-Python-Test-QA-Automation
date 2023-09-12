import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

@pytest.mark.validar
def test_validar():
    nom1="Rodrigo"
    nom2="rodrigo"

    assert nom1==nom2, "Los nombres no son iguales"

@pytest.mark.validarDos
def test_validarDos():
    nom1="Rodrigo"
    nom2="Rodrigo"

    assert nom1==nom2, "Los nombres no son iguales"