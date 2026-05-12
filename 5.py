import random

def countInversions(arr):
    n = len(arr)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def expectedInversions(n):
    return n * (n - 1) / 4

def verifyExperimentally(n, trials=10000):
    total = 0

    for _ in range(trials):
        arr = list(range(1, n + 1))
        random.shuffle(arr)
        total += countInversions(arr)

    empirical = total / trials
    theoretical = expectedInversions(n)

    print(f"n = {n}")
    print(f"Promedio experimental: {empirical}")
    print(f"Valor esperado teórico: {theoretical}")
    print(f"Diferencia: {abs(empirical - theoretical)}")

# Prueba
verifyExperimentally(10)
verifyExperimentally(20)
verifyExperimentally(50)
