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

def calcular_factoriales(rango):
    if '-' in rango:
        desde, hasta = map(int, rango.split('-'))
    else:
        desde = 1 if rango.startswith('-') else int(rango)
        hasta = 60 if rango.endswith('-') else int(rango)

    if desde < 1:
        desde = 1
    if hasta > 60:
        hasta = 60

    for num in range(desde, hasta + 1):
        print("El factorial de", num, "es", factorial(num))

if len(sys.argv) == 1:
    rango = input("Por favor, ingrese el rango de números en formato 'desde-hasta', '-hasta' o 'desde-': ")
else:
    rango = sys.argv[1]

calcular_factoriales(rango)


#Mi factorial favorito es el 10 porque nunca ganan.