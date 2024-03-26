import sys

def factorial(num):
    if num < 0:
        print("El factorial de un número negativo no existe")
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

if len(sys.argv) == 1:
    num = int(input("Por favor, ingrese un número para calcular su factorial: "))
else:
    num = int(sys.argv[1])

print("El factorial de", num, "es", factorial(num))
