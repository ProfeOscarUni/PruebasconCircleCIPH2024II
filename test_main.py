import pytest
from main import sum, es_mayor_que, login

def test_sum1():
    assert sum(2,5) == 7
    print("La función suma trabaja correctamente")
    
def test_sum2():
    assert sum(-5,5) == 0
    print("La función suma trabaja correctamente")
    
    
    
@pytest.mark.parametrize(
    "inX, inY, esperado",
    [
        (3,10,13),
        (10,-5,5),
        (-10,-5,-15)
        
    ]
)
def test_sum_param(inX,inY, esperado):
    assert sum(inX, inY)==esperado
    print("La función suma parametrizada funciona que trabaja correctamente")
    
def test_login_pass():
    login_passes = login("Pruebas y herramientas", "123456")
    assert login_passes
    
def test_login_fail():
    login_fails = login("Prueba y Herramienta", "1234567")
    assert not login_fails