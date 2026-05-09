# Problema 1: Generador Uniforme con Bits Aleatorios

## Enunciado

Implementar `random(a, b)` — un generador de enteros uniformes en el intervalo `[a, b]` — usando únicamente llamadas a `random01()`, donde `P(0) = P(1) = ½`.

---

## Idea central

Para generar un número en `[a, b]` necesito representar `(b − a + 1)` valores distintos. La cantidad mínima de bits para representarlos es:

$$k = \lceil \log_2(b - a + 1) \rceil$$

Con `k` bits puedo generar cualquier número `r ∈ [0, 2^k − 1]`. Si `r` cae dentro del rango válido `[0, b−a]`, lo mapeo a `a + r`. Si no, descarto y repito.

---

## Algoritmo

```
función random(a, b):
    range ← b − a + 1
    k ← ⌈log₂(range)⌉

    repetir:
        r ← 0
        para i en 1..k:
            r ← r * 2 + random01()     // construye número binario bit a bit

        si r < range:
            retornar a + r             // ✓ dentro del rango [a, b]
        // r ≥ range → descartar y volver a intentar
```

### ¿Por qué garantiza uniformidad?

Cada uno de los `2^k` valores posibles de `r` tiene la misma probabilidad `1/2^k` (los bits son independientes y equiprobables). Al descartar los valores fuera de `[0, b−a]` y repetir, condicionamos solo sobre los valores válidos. Como todos los válidos tienen la misma probabilidad de base `1/2^k`, la distribución condicional es uniforme.

---

## Análisis del tiempo esperado

Cada intento es un ensayo Bernoulli independiente con probabilidad de éxito:

$$p = \frac{b - a + 1}{2^k}$$

El número de intentos sigue una **distribución Geométrica** con parámetro `p`:

$$T \sim \text{Geom}(p) \implies E[T] = \frac{1}{p} = \frac{2^k}{b - a + 1}$$

### Cota del valor esperado

Como `k = ⌈log₂(b−a+1)⌉`, se tiene que `2^k < 2(b−a+1)`, por lo tanto:

$$E[\text{intentos}] = \frac{2^k}{b-a+1} < 2$$

El número esperado de intentos es **siempre menor que 2**, independientemente del rango `[a, b]`.

### Complejidad temporal

Cada intento usa exactamente `k` llamadas a `random01()`. Como `k = O(log(b−a+1))` y `E[intentos] < 2`:

$$E[\text{llamadas a random01}] = k \cdot E[\text{intentos}] < 2k = O(\log(b-a+1))$$

> **T(n) ∈ O(log n)** en tiempo esperado, donde `n = b − a + 1` es el tamaño del rango.  
> Si el rango es fijo (p. ej. siempre `[1,6]`), esto es **O(1)** constante.

---

## Ejemplo: `random(1, 6)`

| Parámetro | Valor |
|-----------|-------|
| Rango | 6 valores |
| `k` | `⌈log₂(6)⌉ = 3` bits |
| `r` generado en | `[0, 7]` |
| Válidos (r ≤ 5) | 0,1,2,3,4,5 → retorna 1,2,3,4,5,6 |
| Inválidos | 6, 7 → descartar |
| `p` | `6/8 = 0.75` |
| `E[intentos]` | `1/0.75 ≈ 1.33` |

---

## Verificación empírica

La implementación en Python (`problema1_generador_uniforme.py`) confirma:

1. **Uniformidad**: cada valor aparece aproximadamente `N/(b−a+1)` veces (diferencia < 5%).
2. **Tiempo esperado**: el promedio de intentos simulado coincide con el valor teórico `2^k/(b−a+1)` con error < 1%.

### Salida de ejemplo (`random(1,6)`, N = 10 000):

```
  1: ███████  16.8% ✓
  2: ███████  16.6% ✓
  3: ███████  16.8% ✓
  4: ██████   16.0% ✓
  5: ███████  16.9% ✓
  6: ███████  16.9% ✓

  k = ⌈log₂(6)⌉ = 3 bits
  P(éxito por intento) = 6/8 = 0.7500
  E[intentos] teórico  = 1.3333
  E[intentos] simulado = 1.3366   ✓ (diff = 0.25%)
```

---

## Código

Ver implementación completa en Python: [`problema1_generador_uniforme.py`](./problema1_generador_uniforme.py)

---

## Conclusión

| Propiedad | Resultado |
|-----------|-----------|
| Correctitud | Cada valor en `[a,b]` tiene probabilidad exactamente `1/(b−a+1)` |
| Esperanza de intentos | `< 2` siempre |
| Complejidad | `O(log(b−a+1))` llamadas esperadas a `random01()` |
| Distribución del tiempo | Geométrica(p), `p = (b−a+1)/2^k` |
