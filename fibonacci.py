def fibonacci_recursivo(value):
    if value in (0, 1):
        return value
    return fibonacci_recursivo(value - 1) + fibonacci_recursivo(value - 2)

def fibonacci(value):
    resultado = 0
    anterior = 1
    for _ in range(value):
        resultado += anterior
        anterior = resultado - anterior
    return resultado