import pytest

t=.8

@pytest.mark.run
def test_uno():
    print("Primer test")
    assert True

@pytest.mark.run
def test_dos():
    a=10
    b=10
    assert a==b,"No son iguales"
    assert a!=b,"Son iguales"
    assert a<b,"a no es mayor que b"
    assert a>b,"a no es menor que b"

@pytest.mark.run
def test_tres():
    a=5
    b=10
    assert a==b,"No son iguales"

@pytest.mark.run
def test_cuatro():
    a=15
    b=10
    assert a>b,"a no es mayor que b"

@pytest.mark.run
def test_cinco():
    nombre="Rodri"
    assert nombre=="Rodrigo","El nombre no es Rodrigo"