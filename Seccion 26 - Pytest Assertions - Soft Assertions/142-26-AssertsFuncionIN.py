import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

@pytest.mark.validar
def test_validar():
    dato = "computadora"
    frase = "Dentro de las computadoras hay memoria Ram"

    assert dato in frase, "El dato no esta dentro de la frase"