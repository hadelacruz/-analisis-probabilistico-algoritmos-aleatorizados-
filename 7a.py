import random

# PROBLEMA 7a: guess-sort vs bozo-sort+_opt

def count_bad_pairs(arr):
    bad = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                bad += 1
    return bad

# bozo-sort+_opt: 1 paso = elegir (i,j), intercambiar si es par malo
def bozo_sort_opt_step(arr):
    n = len(arr)
    i = random.randrange(n)
    j = random.randrange(n)
    if i < j and arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
        return True # hubo swap
    return False # paso desperdiciado

# guess-sort: 1 paso = buscar par malo y luego intercambiar
def guess_sort_step(arr):
    n = len(arr)
    comparisons = 0
    while True:
        i = random.randrange(n)
        j = random.randrange(n)
        comparisons += 1
        if i < j and arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            return comparisons

def run_bozo(input_arr):
    arr = list(input_arr)
    steps = 0
    swaps = 0
    MAX_STEPS = 1000000
    while count_bad_pairs(arr) > 0 and steps < MAX_STEPS:
        if bozo_sort_opt_step(arr):
            swaps += 1
        steps += 1
    return steps, swaps

def run_guess(input_arr):
    arr = list(input_arr)
    comparisons = 0
    swaps = 0
    while count_bad_pairs(arr) > 0:
        comparisons += guess_sort_step(arr)
        swaps += 1
    return comparisons, swaps

original = [8, 3, 7, 1, 5, 4, 6, 2]
n = len(original)
max_inversions = n * (n - 1) // 2

bozo_total_steps = 0
bozo_total_swaps = 0
guess_total_comparisons = 0
guess_total_swaps = 0

# Simular 100 veces
for _ in range(100):
    b_steps, b_swaps = run_bozo(original)
    g_comparisons, g_swaps = run_guess(original)
    
    bozo_total_steps += b_steps
    bozo_total_swaps += b_swaps
    guess_total_comparisons += g_comparisons
    guess_total_swaps += g_swaps

print("Comparación (promedio de 100 ensayos):")
print(f"bozo-sort+_opt: {bozo_total_steps // 100} pasos, {bozo_total_swaps // 100} intercambios")
print(f"guess-sort:     {guess_total_comparisons // 100} comparaciones, {guess_total_swaps // 100} intercambios")
print(f"C(n,2) = {max_inversions} — esperado para intercambios")
print("\n¿Por qué guess-sort mejora? Siempre intercambia pares malos.")