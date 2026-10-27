
import pytest
from calculadora import sumar, restar, multiplicar, dividir


def test_sumar_positivos():
    assert sumar(2, 3) == 5


def test_sumar_negativos():
    assert sumar(-2, -3) == -5


def test_dividir_exactamente():
    assert dividir(10, 2) == 5


def test_dividir_decimal():
    assert dividir(7, 2) == 3.5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_dividir_cero_entre_numero():
    assert dividir(0, 5) == 0


def test_dividir_con_texto():
    with pytest.raises(TypeError):
        dividir("diez", 2)


def test_dividir_segundo_argumento_con_texto():
    with pytest.raises(TypeError):
        dividir(10, "dos")


def test_restar_positivos():
    assert restar(8, 3) == 5


def test_restar_negativos():
    assert restar(-2, -3) == 1


def test_multiplicar_positivos():
    assert multiplicar(4, 3) == 12


def test_multiplicar_con_negativo():
    assert multiplicar(-4, 3) == -12
