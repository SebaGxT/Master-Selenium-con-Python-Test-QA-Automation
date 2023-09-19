import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

@pytest.mark.validar
def test_validar():
    a = 25
    b = 25
    if(a==b):
        assert True, "Los datos son iguales"
    else:
        assert False, "Los datos no son iguales"