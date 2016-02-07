class fibo(object):
    def __init__(self,number):
        self.number = number

    def lnum(self):    # escribe la serie Fibonacci hasta n
        a, b = 0, 1
        while b < self.number:
            print b,
            a, b = b, a+b

    def array(self): # devuelve la serie Fibonacci hasta n
        resultado = []
        a, b = 0, 1
        while b < self.number:
            resultado.append(b)
            a, b = b, a+b
        return resultado
