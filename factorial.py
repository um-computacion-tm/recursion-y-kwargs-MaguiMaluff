def factorial_recursivo(value):
    if value < 2:
        return 1
    return value * factorial_recursivo(value - 1)

def factorial(value):
    resultado = value
    if value == 0:
        return 1
    while value > 2:
        value -= 1
        resultado *= value
    return resultado
