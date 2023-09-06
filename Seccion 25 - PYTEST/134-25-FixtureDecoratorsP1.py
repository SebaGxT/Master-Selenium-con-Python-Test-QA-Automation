import pytest

@pytest.fixture(scope='module')
def setup_login_uno():
    print("\n\nEmpezando el login del sistema uno\n")
    yield
    print("\n\nSaliendo del sistema prueba ok\n")

@pytest.fixture(scope='module')
def setup_login_dos():
    print("\n\nEmpezando las pruebas del sistema dos\n")
    yield
    print("\n\nFin de las pruebas del sistema dos\n")

def test_uno(setup_login_uno):
    print("\n##### Empezando las pruebas del test uno #####\n")

def test_dos(setup_login_dos):
    print("\n@@@@@ Empezando las pruebas del test dos @@@@@\n")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("\n\nPrueba tres del modulo login dos\n\n")