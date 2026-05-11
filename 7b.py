import random
import math

# PROBLEMA 7b: Fun-Sort y verificación de tiempo de ejecución


def count_inversions(arr):
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def fun_sort(input_arr):
    a = list(input_arr)
    n = len(a)
    comparisons = 0
    swaps = 0

    # Fun-Sort se ejecuta hasta que ya no haya inversiones (F = 0)
    while count_inversions(a) > 0:
        for i in range(n):
            x = a[i]
            l = -1
            h = n

            # Búsqueda binaria O(log n)
            while l + 1 < h:
                m = (l + h) // 2
                comparisons += 1
                if x <= a[m]:
                    h = m
                else:
                    l = m

            if h < i and a[h] != x:
                
                a[i], a[h] = a[h], a[i]
                swaps += 1
            elif h > i:
                
                target = h - 1
                if target > i and a[target] != x:
                    a[i], a[target] = a[target], a[i]
                    swaps += 1

    return a, comparisons, swaps


tests = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
]

print("=== 1. Verificación del Runtime Experimental ===")
for arr in tests:
    F_inicial = count_inversions(arr)
    sorted_arr, total_comp, total_swaps = fun_sort(arr)
    n_size = len(arr)
    bound = (n_size + F_inicial) * math.log2(n_size)
    
    print(f"Input: {arr}")
    print(f"  Inversiones (F) = {F_inicial}")
    print(f"  Comparaciones Reales = {total_comp}")
    print(f"  Cota Teórica O((n+F)logn) ≈ {int(bound)}")
    print(f"  Resultado Ordenado: {sorted_arr}\n")


n_val = 8
total_F_simulado = 0
intentos = 10000

print("Calculando simulación de 10,000 arreglos, por favor espera un segundo...")

for _ in range(intentos):
    lista_aleatoria = list(range(1, n_val + 1))
    random.shuffle(lista_aleatoria)
    total_F_simulado += count_inversions(lista_aleatoria)

e_f_simulado = total_F_simulado / intentos
e_f_teorico = n_val * (n_val - 1) / 4
umbral_teorema = (n_val * n_val) / math.log2(n_val)

print("\n=== 2. Análisis del Teorema 6 (n=8) ===")
print(f"E[F] simulado (Caso Promedio): {e_f_simulado:.2f}")
print(f"E[F] teórico (n*(n-1)/4): {int(e_f_teorico)}")
print(f"Umbral del Teorema 6 (n²/logn): {umbral_teorema:.2f}")

if e_f_simulado < umbral_teorema:
    print("\nResultado: Para n=8, el promedio de inversiones está POR DEBAJO del umbral.")