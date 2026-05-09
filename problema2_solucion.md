# Problema 2: Truco de Von Neumann — Dessesgando una moneda

## Enunciado

Dado `biasedRandom(p)` que produce `1` con probabilidad `p` y `0` con probabilidad `1−p` (con `0 < p < 1`), diseñar un algoritmo que produzca `0` o `1` cada uno con probabilidad exactamente `½`, calculando su tiempo de ejecución esperado.

---

## Idea central (Truco de Von Neumann, 1951)

### Observación clave

Llamar a `biasedRandom(p)` **dos veces** y observar el par `(a, b)`. Las probabilidades de cada par son:

| Par `(a, b)` | Probabilidad | Acción |
|:---:|:---:|:---:|
| `(1, 0)` | `p · (1−p)` | → emite **1** |
| `(0, 1)` | `(1−p) · p` | → emite **0** |
| `(0, 0)` | `(1−p)²` | → DESCARTA |
| `(1, 1)` | `p²` | → DESCARTA |

La clave está en que:

$$P(1,0) = p(1-p) = (1-p)p = P(0,1)$$

Los pares "cruzados" tienen **exactamente la misma probabilidad**, sin importar el valor de `p`. Si solo emitimos cuando aparece uno de estos pares, la probabilidad condicional de cada uno es `½`.

---

## Algoritmo

```
función unbiasedRandom(p):
    repetir:
        a ← biasedRandom(p)
        b ← biasedRandom(p)

        si (a = 1) y (b = 0): retornar 1    // par (1,0)
        si (a = 0) y (b = 1): retornar 0    // par (0,1)
        // par (0,0) o (1,1): descartar y repetir
```

### ¿Por qué la salida es 50/50?

Sea el evento "emitir resultado". Dado que emitimos:

$$P(\text{salida} = 1 \mid \text{emitimos}) = \frac{P(1,0)}{P(1,0) + P(0,1)} = \frac{p(1-p)}{p(1-p) + (1-p)p} = \frac{p(1-p)}{2p(1-p)} = \frac{1}{2}$$

La simetría es exacta y algebraica, no aproximada.

---

## Análisis del tiempo esperado

Cada par `(a, b)` es un intento. La probabilidad de emitir en un intento es:

$$P(\text{emitir}) = P(1,0) + P(0,1) = 2p(1-p)$$

El número de intentos sigue una **distribución Geométrica**:

$$E[\text{intentos}] = \frac{1}{2p(1-p)}$$

Como cada intento usa **2 llamadas** a `biasedRandom`:

$$E[\text{llamadas a biasedRandom}] = \frac{2}{2p(1-p)} = \frac{1}{p(1-p)}$$

### Comportamiento según `p`

| `p` | `E[llamadas]` = `1/(p(1−p))` | Observación |
|:---:|:---:|---|
| 0.01 | ≈ 101 | Moneda muy sesgada → muy ineficiente |
| 0.10 | ≈ 11.1 | |
| 0.30 | ≈ 4.76 | |
| **0.50** | **4.00** | **Mínimo global** |
| 0.70 | ≈ 4.76 | Simétrico respecto a p=0.5 |
| 0.90 | ≈ 11.1 | |
| 0.99 | ≈ 101 | Moneda muy sesgada → muy ineficiente |

El mínimo se obtiene cuando `p = ½`, con `E = 4` llamadas.

> **Cuando `p → 0` o `p → 1`**: los pares útiles `(0,1)` y `(1,0)` se vuelven rarísimos. Casi siempre sale `(0,0)` o `(1,1)` respectivamente, y se necesitan muchos más intentos. El algoritmo sigue siendo **correcto** pero cada vez **menos eficiente**.

---

## Verificación empírica

La implementación en Python (`problema2_von_neumann.py`) confirma para N = 5 000 muestras:

```
  p=0.1  →  salida: 49.6% unos  ✓  |  E[calls] simulado= 10.93  teórico= 11.11 ✓
  p=0.3  →  salida: 50.5% unos  ✓  |  E[calls] simulado=  4.75  teórico=  4.76 ✓
  p=0.5  →  salida: 49.7% unos  ✓  |  E[calls] simulado=  4.02  teórico=  4.00 ✓
  p=0.7  →  salida: 50.1% unos  ✓  |  E[calls] simulado=  4.74  teórico=  4.76 ✓
  p=0.9  →  salida: 49.2% unos  ✓  |  E[calls] simulado= 11.09  teórico= 11.11 ✓
```

1. La salida es siempre ~50/50 sin importar `p`. ✓
2. El promedio de llamadas coincide con el valor teórico (error < 2%). ✓

---

## Código

Ver implementación completa en Python: [`problema2_von_neumann.py`](./problema2_von_neumann.py)

---

## Conexión con el Problema 1

Ambos problemas usan el mismo patrón:

| Aspecto | Problema 1 | Problema 2 |
|---|---|---|
| Recurso base | `random01()` (justo) | `biasedRandom(p)` (sesgado) |
| Truco | Generar `r` y descartar si sale del rango | Generar par y descartar si es `(0,0)` o `(1,1)` |
| Distribución del # intentos | Geométrica(`(b−a+1)/2^k`) | Geométrica(`2p(1−p)`) |
| Garantía de uniformidad | Todos los valores válidos tienen igual prob. de base | Simetría: `P(1,0) = P(0,1)` siempre |

---

## Conclusión

| Propiedad | Resultado |
|-----------|-----------|
| Correctitud | La salida es exactamente 50/50 para cualquier `0 < p < 1` |
| `E[llamadas]` | `1/(p(1-p))`, mínimo en `p=0.5` → `E=4` |
| Comportamiento extremo | Cuando `p → 0` o `p → 1`, `E[llamadas] → ∞` |
| Complejidad temporal | `T ~ Geom(2p(1-p))`, `O(1)` esperado para `p` fijo |
| Principio usado | Simetría algebraica + independencia de llamadas |
