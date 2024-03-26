import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def calcular_collatz_para_rango(rango):
    resultados = {}
    for num in range(1, rango + 1):
        resultados[num] = collatz(num)
    return resultados

def graficar_collatz(resultados):
    plt.figure(figsize=(10, 6))
    plt.scatter(resultados.keys(), resultados.values(), s=5, c='blue')
    plt.title('Número de Collatz para los números entre 1 y 10000')
    plt.xlabel('Número de comienzo de la secuencia (n)')
    plt.ylabel('Número de iteraciones para converger')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    resultados = calcular_collatz_para_rango(10000)
    graficar_collatz(resultados)
