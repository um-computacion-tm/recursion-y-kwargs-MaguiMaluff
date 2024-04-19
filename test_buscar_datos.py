import unittest
from buscar_datos import buscar_datos

class TestsFibonacci(unittest.TestCase):
    database = {
            '1':{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            '2':{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            '3':{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            }
                }
    
    def test_0(self):
        resultado = buscar_datos("Pablo", "Diego","Ruiz","Picasso", **self.database)
        self.assertEqual(resultado, 1)
    
    def test_1(self):
        resultado = buscar_datos("Marcos", "Marcelo","Luciano","Elias","Gonzalez",**self.database)
        self.assertEqual(resultado, 3)

    def test_3(self):
        resultado = buscar_datos("Pepe", **self.database)
        self.assertEqual(resultado, 'No se encontró')



unittest.main()
