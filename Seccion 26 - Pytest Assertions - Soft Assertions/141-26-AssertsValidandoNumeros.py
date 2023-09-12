import pytest
from Funciones_Globales.funciones import Funciones_Globales as FG

@pytest.mark.validar
def test_validar():
    a=21
    b=23
    c=18

    assert a<=b or a<=c , "A no es menor o igual que B o A no es menor o igual que C"