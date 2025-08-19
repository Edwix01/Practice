class Calculadora:
    sumar = lambda self, a, b: a + b
    restar = lambda self, a, b: a - b

c = Calculadora()
print(c.sumar(2, 3))   # 5
print(c.restar(7, 2))  # 5
