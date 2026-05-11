import random
import math

# ════════════════════════════════════════════════════
# PROBLEMA 3: Hiring Problem — probabilidades y esperanza
# ════════════════════════════════════════════════════
#
# ALGORITMO:
#   best = -inf
#   para i = 1 hasta n:
#     entrevistar candidato i
#     si calidad[i] > best:
#       best = calidad[i]
#       CONTRATAR candidato i
#
# ANÁLISIS CON INDICADORAS:
#   Sea Xi = 1 si el candidato i es contratado.
#   Candidato i se contrata si es MEJOR que los i-1 anteriores.
#   En permutación aleatoria: P(Xi = 1) = 1/i
#   → E[X] = Σ 1/i = Hn ≈ ln(n)
#
# CASOS EXTREMOS:
#   Best-case  (1 contratación):  candidato 1 es el mejor → P = 1/n
#   Worst-case (n contrataciones): orden creciente          → P = 1/n!


# Simula el hiring problem y cuenta contrataciones e índices de contratados.
def hiring_algorithm(candidates):
    best = float('-inf')
    hires = 0
    hired = []

    for i, quality in enumerate(candidates):
        if quality > best:
            best = quality
            hires += 1
            hired.append(i)

    return hires, hired


# ── Prueba manual ─────────────────────────────────────
test = [3, 7, 2, 9, 1, 8, 5, 4]
hires, hired = hiring_algorithm(test)

print("Candidatos (en orden de llegada):", test)
print(f"Contrataciones: {hires} — índices: {hired}")
print(f"Calificaciones contratadas: {[test[i] for i in hired]}")
print("(Cada contratado es mejor que todos los anteriores)\n")


# ── Simulación para verificar E[X] = Hn ≈ ln(n) ──────
n = 8
TRIALS = 100_000

# Número armónico Hn
Hn = sum( 1 / ( i + 1 ) for i in range( n) )

# Factorial para worst-case
n_factorial = math.factorial(n )

total_hires = 0
best_case_count = 0
worst_case_count = 0

candidates = list(range( 1, n + 1) )

for _ in range(TRIALS):
    perm = candidates[:]
    random.shuffle(perm )

    h, _ = hiring_algorithm( perm)
    total_hires += h

    if h == 1:
        best_case_count += 1
    if h == n:
        worst_case_count += 1


print(f"Simulación (n={n}, {TRIALS:,} ensayos):")
print(f"  E[contrataciones] simulado : {total_hires / TRIALS:.4f}")
print(f"  Hn (valor teórico)         : {Hn:.4f}")
print(f"  ln(n) ≈                    : {math.log(n):.4f}")
print()
print(f"  P(best-case = 1 hire) simulado : {best_case_count / TRIALS:.4f}")
print(f"  P(best-case) teórico = 1/n     : {1 / n:.4f}")
print()
print(f"  P(worst-case = n hires) simulado : {worst_case_count / TRIALS:.6f}")
print(f"  P(worst-case) teórico = 1/n!     : {1 / n_factorial:.6f}")