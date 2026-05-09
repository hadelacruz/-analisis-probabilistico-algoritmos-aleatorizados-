
import random
import math
from collections import Counter


# ─────────────────────────────────────────────
# Generador base: moneda justa
# ─────────────────────────────────────────────
def random01() -> int:
    """Lanzamiento de moneda justa: retorna 0 o 1 con P=0.5 cada uno."""
    return 0 if random.random() < 0.5 else 1


# ─────────────────────────────────────────────
# Generador uniforme en [a, b]
# ─────────────────────────────────────────────
def random_uniform(a: int, b: int) -> tuple[int, int]:
    range_size = b - a + 1
    k = math.ceil(math.log2(range_size)) if range_size > 1 else 1

    attempts = 0
    while True:
        attempts += 1
        # Construir r leyendo k bits en binario
        r = 0
        for _ in range(k):
            r = r * 2 + random01()
        # r ∈ [0, 2^k - 1]

        if r < range_size:
            return a + r, attempts
        # Fuera de rango → descartar (garantiza uniformidad)


# ─────────────────────────────────────────────
# Verificación empírica
# ─────────────────────────────────────────────
def verificar(a: int, b: int, n: int = 10_000) -> None:
    print(f"\n{'═'*55}")
    print(f"  random({a}, {b})  —  {n:,} muestras")
    print(f"{'═'*55}")

    conteos: Counter = Counter()
    total_intentos = 0

    for _ in range(n):
        val, intentos = random_uniform(a, b)
        conteos[val] += 1
        total_intentos += intentos

    # Distribución
    print("\nDistribución de salida:")
    esperado = n / (b - a + 1)
    for v in range(a, b + 1):
        c = conteos[v]
        pct = c / n * 100
        barra = "█" * round(c / n * 40)
        marca = " ✓" if abs(c - esperado) / esperado < 0.05 else " ⚠"
        print(f"  {v:3d}: {barra:<42} {pct:5.1f}%{marca}")

    # Análisis teórico
    range_size = b - a + 1
    k = math.ceil(math.log2(range_size)) if range_size > 1 else 1
    p = range_size / (2 ** k)
    e_teorico = 1 / p
    e_simulado = total_intentos / n

    print(f"\nAnálisis de tiempo esperado:")
    print(f"  k = ⌈log₂({range_size})⌉ = {k} bits")
    print(f"  2^k = {2**k}  →  {2**k - range_size} valores descartados de {2**k}")
    print(f"  P(éxito por intento) = {range_size}/{2**k} = {p:.4f}")
    print(f"  E[intentos] teórico  = 1/p = {e_teorico:.4f}")
    print(f"  E[intentos] simulado = {e_simulado:.4f}")
    diferencia = abs(e_simulado - e_teorico) / e_teorico * 100
    print(f"  Diferencia           = {diferencia:.2f}%  {'✓' if diferencia < 5 else '⚠'}")
    print(f"\n  Complejidad temporal: T(n) ∈ O(1) esperado")
    print(f"  (constante — no depende del tamaño del rango)")


# ─────────────────────────────────────────────
# Casos de prueba
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("PROBLEMA 1: Generador Uniforme con Bits Aleatorios")
    print("Truco: k bits → Geométrica(p) para garantizar uniformidad\n")

    # Dado justo
    verificar(1, 6)

    # Potencia de 2 exacta (sin descarte)
    verificar(0, 3)

    # Rango asimétrico
    verificar(5, 10)

    # Rango con muchos descartes posibles
    verificar(0, 4)   # k=3 → 2^3=8, 3 valores descartados → p=5/8=0.625

    print(f"\n{'═'*55}")
    print("  Conclusión")
    print(f"{'═'*55}")
    print("  • La distribución es uniforme para todo [a, b].")
    print("  • E[intentos] ≤ 2  (ya que 2^k < 2·(b-a+1)).")
    print("  • T(n) = O(1) esperado → independiente del rango.")
