class Calc(object):
    def __init__(self,number):
        self.number = number

    def fib(self):    # escribe la serie Fibonacci hasta n
        a, b = 0, 1
        while b < self.number:
            print b,
            a, b = b, a+b

    def fib2(self): # devuelve la serie Fibonacci hasta n
        resultado = []
        a, b = 0, 1
        while b < self.number:
            resultado.append(b)
            a, b = b, a+b
        return resultado
