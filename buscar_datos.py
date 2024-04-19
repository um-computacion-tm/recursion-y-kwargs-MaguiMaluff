###La funcion no imprime nada, con los 
###tests en test_buscar_nombre.py se verifica que funciona

def buscar_datos(*args, **kwargs):
    sum = 0
    for kwarg in kwargs:
        items = kwargs[kwarg].values()
        for arg in args:
            if arg not in items:
                break
            else:
                sum += 1
                if sum == len(items) and sum == len(args):
                    return int(kwarg)
    return 'No se encontró'
