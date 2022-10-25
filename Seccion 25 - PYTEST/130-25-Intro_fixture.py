from Funciones_Globales.funciones import Funciones_Globales as FG

global Fun

def setup_function(function):
    print("\n\n Esto va al inicio de cada test \n")

def teardown_function(function):
    print("\n\n Esto va al final de cada test \n")

def test_uno():
    print("Test uno")

def test_dos():
    print("Test dos")

def test_tres():
    print("Test tres")

def test_cuatro():
    print("Test cuatro")