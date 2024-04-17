def sumatoria_recursiva(value):
    if value == 0:
        return 0
    return value + sumatoria_recursiva(value - 1)

def sumatoria(value):
    resultado = value
    while value > 0:
        value = value - 1
        resultado += value
    return resultado