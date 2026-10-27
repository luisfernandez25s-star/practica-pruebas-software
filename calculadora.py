
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("El primer argumento debe ser numérico")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("El segundo argumento debe ser numérico")

    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    return a / b
