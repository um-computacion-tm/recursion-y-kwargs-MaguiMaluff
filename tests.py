import unittest
from sumatoria import sumatoria, sumatoria_recursiva
from factorial import factorial, factorial_recursivo
from fibonacci import fibonacci, fibonacci_recursivo

### Tests para funciones Fibonacci, Factorial y Sumatoria

class TestsFibonacci(unittest.TestCase):
    def test_0(self):
        resultado_1 = fibonacci(0)
        resultado_2 = fibonacci_recursivo(0)
        self.assertEqual(resultado_1, 0)
        self.assertEqual(resultado_2, 0)

    def test_1(self):
        resultado_1 = fibonacci(1)
        resultado_2 = fibonacci_recursivo(1)
        self.assertEqual(resultado_1, 1)
        self.assertEqual(resultado_2, 1)

    def test_2(self):
        resultado_1 = fibonacci(2)
        resultado_2 = fibonacci_recursivo(2)
        self.assertEqual(resultado_1, 1)
        self.assertEqual(resultado_2, 1)

    def test_3(self):
        resultado_1 = fibonacci(3)
        resultado_2 = fibonacci_recursivo(3)
        self.assertEqual(resultado_1, 2)
        self.assertEqual(resultado_2, 2)

    def test_4(self):
        resultado_1 = fibonacci(4)
        resultado_2 = fibonacci_recursivo(4)
        self.assertEqual(resultado_1, 3)
        self.assertEqual(resultado_2, 3)

    def test_5(self):
        resultado_1 = fibonacci(5)
        resultado_2 = fibonacci_recursivo(5)
        self.assertEqual(resultado_1, 5)
        self.assertEqual(resultado_2, 5)

    def test_6(self):
        resultado_1 = fibonacci(6)
        resultado_2 = fibonacci_recursivo(6)
        self.assertEqual(resultado_1, 8)
        self.assertEqual(resultado_2, 8)

    def test_7(self):
        resultado_1 = fibonacci(7)
        resultado_2 = fibonacci_recursivo(7)
        self.assertEqual(resultado_1, 13)
        self.assertEqual(resultado_2, 13)

    def test_8(self):
        resultado_1 = fibonacci(8)
        resultado_2 = fibonacci_recursivo(8)
        self.assertEqual(resultado_1, 21)
        self.assertEqual(resultado_2, 21)

    def test_9(self):
        resultado_1 = fibonacci(9)
        resultado_2 = fibonacci_recursivo(9)
        self.assertEqual(resultado_1, 34)
        self.assertEqual(resultado_2, 34)

    def test_10(self):
        resultado_1 = fibonacci(10)
        resultado_2 = fibonacci_recursivo(10)
        self.assertEqual(resultado_1, 55)
        self.assertEqual(resultado_2, 55)

    def test_11(self):
        resultado_1 = fibonacci(11)
        resultado_2 = fibonacci_recursivo(11)
        self.assertEqual(resultado_1, 89)
        self.assertEqual(resultado_2, 89)

    def test_12(self):
        resultado_1 = fibonacci(12)
        resultado_2 = fibonacci_recursivo(12)
        self.assertEqual(resultado_1, 144)
        self.assertEqual(resultado_2, 144)

    def test_13(self):
        resultado_1 = fibonacci(13)
        resultado_2 = fibonacci_recursivo(13)
        self.assertEqual(resultado_1, 233)
        self.assertEqual(resultado_2, 233)

class TestsFactorial(unittest.TestCase):
    def test_0(self):
        resultado_1 = factorial(0)
        resultado_2 = factorial_recursivo(0)
        self.assertEqual(resultado_1, 1)
        self.assertEqual(resultado_2, 1)
    
    def test_1(self):
        resultado_1 = factorial(1)
        resultado_2 = factorial_recursivo(1)
        self.assertEqual(resultado_1, 1)
        self.assertEqual(resultado_2, 1)

    def test_2(self):
        resultado_1 = factorial(2)
        resultado_2 = factorial_recursivo(2)
        self.assertEqual(resultado_1, 2)
        self.assertEqual(resultado_2, 2)
    
    def test_3(self):
        resultado_1 = factorial(3)
        resultado_2 = factorial_recursivo(3)
        self.assertEqual(resultado_1, 6)
        self.assertEqual(resultado_2, 6)

    def test_4(self):
        resultado_1 = factorial(4)
        resultado_2 = factorial_recursivo(4)
        self.assertEqual(resultado_1, 24)
        self.assertEqual(resultado_2, 24)
    
    def test_5(self):
        resultado_1 = factorial(5)
        resultado_2 = factorial_recursivo(5)
        self.assertEqual(resultado_1, 120)
        self.assertEqual(resultado_2, 120)

class TestsSumatoria(unittest.TestCase):
    def test_0(self):
        resultado_1 = sumatoria(0)
        resultado_2 = sumatoria_recursiva(0)
        self.assertEqual(resultado_1, 0)
        self.assertEqual(resultado_2, 0)

    def test_1(self):
        resultado_1 = sumatoria(1)
        resultado_2 = sumatoria_recursiva(1)
        self.assertEqual(resultado_1, 1)
        self.assertEqual(resultado_2, 1)

    def test_2(self):
        resultado_1 = sumatoria(2)
        resultado_2 = sumatoria_recursiva(2)
        self.assertEqual(resultado_1, 3)
        self.assertEqual(resultado_2, 3)

    def test_3(self):
        resultado_1 = sumatoria(3)
        resultado_2 = sumatoria_recursiva(3)
        self.assertEqual(resultado_1, 6)
        self.assertEqual(resultado_2, 6)

    def test_4(self):
        resultado_1 = sumatoria(4)
        resultado_2 = sumatoria_recursiva(4)
        self.assertEqual(resultado_1, 10)
        self.assertEqual(resultado_2, 10)

    def test_5(self):
        resultado_1 = sumatoria(5)
        resultado_2 = sumatoria_recursiva(5)
        self.assertEqual(resultado_1, 15)
        self.assertEqual(resultado_2, 15)

    def test_6(self):
        resultado_1 = sumatoria(6)
        resultado_2 = sumatoria_recursiva(6)
        self.assertEqual(resultado_1, 21)
        self.assertEqual(resultado_2, 21)


    

unittest.main()