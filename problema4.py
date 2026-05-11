import random

# ══════════════════════════════════════════════════
# PROBLEMA 4: Suma esperada de n dados con indicadoras
# ══════════════════════════════════════════════════
#
# SETUP:
#   X = suma de n dados
#   X = X1 + X2 + ... + Xn  (Xi = valor del dado i)
#
# USANDO LINEALIDAD DE LA ESPERANZA:
#   E[X] = E[X1] + E[X2] + ... + E[Xn]
#        = n · E[X1]                   (todos idénticos)
#        = n · (1+2+3+4+5+6)/6
#        = n · 3.5
#
# USANDO VARIABLES INDICADORAS (enfoque más formal):
#   Sea Yij = 1 si dado i muestra cara j, 0 si no
#   E[Yij] = P(Yij = 1) = 1/6
#   Xi = Σj=1..6  j · Yij
#   E[Xi] = Σj=1..6  j · E[Yij] = Σj=1..6  j · (1/6) = 3.5


def lanzar_dado():
    return random.randint( 1, 6 )


# Calcula E[suma de n dados] usando variables indicadoras.
def expected_sum(n):
    E_dado = sum( j * (1 / 6 ) for j in range(1, 7 ))  # = 3.5
    return n * E_dado # linealidad de la esperanza


# Simula lanzar n dados 'trials' veces y retorna el promedio de sumas.
def simular_n_dados(n, trials=20_000):
    total = 0

    for _ in range( trials):
        total += sum( lanzar_dado() for _ in range( n) )
    return total / trials


# ── Verificación ──────────────────────────────────
TRIALS = 20_000
print("Verificando E[suma] = 3.5·n:\n")
print(f"{'n':>5} | {'Teórico':>8} | {'Simulado':>10}")
print("-" * 30)

for n in [1, 2, 5, 10, 20, 100 ]:
    teorico = expected_sum( n)
    simulado = simular_n_dados(n, TRIALS )
    print(f"{n:>5} | {teorico:>8.1f} | {simulado:>10.3f}")

# ── Demostración de la linealidad ─────────────────
print("\nPoder de la linealidad:")
print("E[X1 + X2] = E[X1] + E[X2] = 3.5 + 3.5 = 7")
print("Esto funciona SIN importar si los dados son independientes o no.")
print("Solo necesitamos E[cada Xi] — no hace falta la distribución conjunta.")