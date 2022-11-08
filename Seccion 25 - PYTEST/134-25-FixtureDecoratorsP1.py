import pytest

@pytest.fixture(scope='module')
def setup_login_uno():
    print("\nEmpezando el login del sistema uno\n")
    yield
    print("\nSaliendo del sistema prueba ok")

@pytest.fixture(scope='module')
def setup_login_dos():
    print("\nEmpezando las pruebas del sistema dos")
    yield
    print("\nFin de las pruebas del sistema dos")

def test_uno(setup_login_uno):
    print("\nEmpezando las pruebas del test uno")

def test_dos(setup_login_dos):
    print("\nEmpezando las pruebas del test dos")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("\nPrueba tres del modulo login dos")