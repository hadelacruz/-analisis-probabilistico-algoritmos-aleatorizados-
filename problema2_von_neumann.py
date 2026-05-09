import random
import math
from dataclasses import dataclass


# ─────────────────────────────────────────────
# Generador sesgado base
# ─────────────────────────────────────────────
def biased_random(p: float) -> int:
    return 1 if random.random() < p else 0


# ─────────────────────────────────────────────
# Generador sin sesgo (Von Neumann)
# ─────────────────────────────────────────────
@dataclass
class Resultado:
    bit: int
    llamadas: int


def unbiased_random(p: float) -> Resultado:
    llamadas = 0
    while True:
        a = biased_random(p); llamadas += 1
        b = biased_random(p); llamadas += 1

        if a == 1 and b == 0:
            return Resultado(bit=1, llamadas=llamadas)  # par (1,0) → 1
        if a == 0 and b == 1:
            return Resultado(bit=0, llamadas=llamadas)  # par (0,1) → 0
        # Par (0,0) o (1,1): descartar y repetir


# ─────────────────────────────────────────────
# Verificación empírica
# ─────────────────────────────────────────────
def verificar(p: float, n: int = 5_000) -> None:
    unos = 0
    total_llamadas = 0

    for _ in range(n):
        r = unbiased_random(p)
        unos += r.bit
        total_llamadas += r.llamadas

    pct_unos = unos / n * 100
    pct_ceros = (n - unos) / n * 100
    avg_llamadas = total_llamadas / n
    teorico = 1 / (p * (1 - p))

    desviacion = abs(pct_unos - 50)
    ok_dist = "✓" if desviacion < 2.5 else "⚠"
    ok_calls = "✓" if abs(avg_llamadas - teorico) / teorico < 0.05 else "⚠"

    print(f"  p={p:.1f}  |  "
          f"0: {pct_ceros:5.1f}%  1: {pct_unos:5.1f}% {ok_dist}  |  "
          f"E[calls] simulado={avg_llamadas:6.2f}  teórico={teorico:6.2f} {ok_calls}")


def verificar_detallado(p: float, n: int = 5_000) -> None:
    print(f"\n{'─'*55}")
    print(f"  Análisis detallado para p = {p}")
    print(f"{'─'*55}")

    # Probabilidades teóricas
    p10 = p * (1 - p)
    p01 = (1 - p) * p
    p00 = (1 - p) ** 2
    p11 = p ** 2

    print(f"\n  Probabilidades de cada par:")
    print(f"    P(1,0) = p·(1-p)  = {p10:.4f}  → emite 1")
    print(f"    P(0,1) = (1-p)·p  = {p01:.4f}  → emite 0")
    print(f"    P(0,0) = (1-p)²   = {p00:.4f}  → descarta")
    print(f"    P(1,1) = p²       = {p11:.4f}  → descarta")
    print(f"    Suma              = {p10+p01+p00+p11:.4f}")

    p_emitir = 2 * p * (1 - p)
    e_llamadas = 1 / (p * (1 - p))
    print(f"\n  P(emitir en un intento) = 2·p·(1-p) = {p_emitir:.4f}")
    print(f"  E[llamadas] = 1/(p·(1-p)) = {e_llamadas:.4f}")

    # Simulación
    unos = 0
    total_llamadas = 0
    for _ in range(n):
        r = unbiased_random(p)
        unos += r.bit
        total_llamadas += r.llamadas

    print(f"\n  Simulación ({n:,} muestras):")
    print(f"    Salida: {unos/n*100:.1f}% unos, {(n-unos)/n*100:.1f}% ceros  "
          f"{'✓ (≈50/50)' if abs(unos/n - 0.5) < 0.025 else '⚠ sesgo detectado'}")
    print(f"    E[llamadas] simulado = {total_llamadas/n:.4f}")
    print(f"    E[llamadas] teórico  = {e_llamadas:.4f}")


# ─────────────────────────────────────────────
# Análisis del comportamiento cuando p → 0 o p → 1
# ─────────────────────────────────────────────
def analisis_extremos() -> None:
    print(f"\n{'═'*55}")
    print("  Comportamiento cuando p → 0 o p → 1")
    print(f"{'═'*55}")
    print(f"\n  {'p':>6}  {'E[llamadas] teórico':>22}  {'Interpretación'}")
    print(f"  {'─'*6}  {'─'*22}  {'─'*25}")
    valores = [0.01, 0.05, 0.10, 0.30, 0.50, 0.70, 0.90, 0.95, 0.99]
    for p in valores:
        e = 1 / (p * (1 - p))
        bar = "█" * min(int(e / 2), 30)
        print(f"  {p:>6.2f}  {e:>22.1f}  {bar}")
    print("\n  → Cuanto más sesgada la moneda, más llamadas se necesitan.")
    print("  → El mínimo es E=4 cuando p=0.5 (moneda justa).")


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("PROBLEMA 2: Truco de Von Neumann — Dessesgando una moneda")
    print("Idea: P(1,0) = P(0,1) = p(1-p) sin importar p → salida 50/50\n")

    print(f"{'═'*55}")
    print("  Tabla resumen — {N=5,000 muestras}")
    print(f"{'═'*55}")
    print(f"  {'p':>4}  {'distribución salida':>26}  {'E[llamadas]':>24}")
    print(f"  {'─'*4}  {'─'*26}  {'─'*24}")

    for p in [0.1, 0.2, 0.3, 0.5, 0.7, 0.9]:
        verificar(p)

    # Análisis detallado para un caso
    verificar_detallado(p=0.3)

    # Comportamiento en extremos
    analisis_extremos()

    print(f"\n{'═'*55}")
    print("  Conclusión")
    print(f"{'═'*55}")
    print("  • La salida siempre es ~50/50, sin importar p.")
    print("  • Solo se necesita 0 < p < 1 (excluir monedas triviales).")
    print("  • E[llamadas] = 1/(p(1-p)) crece cuando p → 0 o p → 1.")
    print("  • Von Neumann, 1951: solo independencia + simetría bastan.")
