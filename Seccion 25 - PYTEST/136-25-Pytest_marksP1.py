import pytest

@pytest.mark.run
def test_uno():
    print("Test uno")

@pytest.mark.run
def test_dos():
    print("Test dos")

@pytest.mark.run
def test_tres():
    print("Test tres")

@pytest.mark.notrun
def test_cuatro():
    print("Test cuatro")

@pytest.mark.notrun
def test_cinco():
    print("Test cinco")

@pytest.mark.run
def test_seis():
    print("Test seis")

@pytest.mark.skip
def test_siete():
    print("Test siete")