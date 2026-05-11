# Problema 3: Hiring Problem

## Enunciado

El algoritmo entrevista candidatos en orden aleatorio y contrata al candidato `i` si es mejor que todos los anteriores. ¿Cuáles son las probabilidades del best-case (contratar solo 1 vez) y del worst-case (contratar `n` veces)? ¿Cuántas contrataciones se esperan en promedio?

---

## Idea central

El primer candidato siempre se contrata (no hay con quién compararlo). Después, el candidato `i` se contrata si y solo si es el mejor entre los primeros `i`.

En una permutación aleatoria uniforme, cada uno de los `i` primeros candidatos tiene la misma probabilidad de ser el mejor, por lo tanto:

$$P(\text{candidato } i \text{ es contratado}) = \frac{1}{i}$$

---

## Casos extremos

**Best-case — 1 sola contratación:** para que esto pase, el candidato 1 debe ser el mejor de todos los `n`. La probabilidad de que el primero en llegar sea el mejor es:

$$P(\text{best-case}) = \frac{1}{n}$$

**Worst-case — `n` contrataciones:** ocurre cuando los candidatos llegan en orden creciente de calidad (cada uno mejor que el anterior). De las `n!` permutaciones posibles, solo 1 tiene este orden:

$$P(\text{worst-case}) = \frac{1}{n!}$$

Para `n = 8`: P(best) = 0.125, P(worst) = 1/40320 ≈ 0.0000248.

---

## Esperanza con variables indicadoras

Sea $X_i = 1$ si el candidato $i$ es contratado. Por linealidad de la esperanza:

$$E[\text{contrataciones}] = \sum_{i=1}^{n} E[X_i] = \sum_{i=1}^{n} \frac{1}{i} = H_n \approx \ln(n)$$

donde $H_n$ es el $n$-ésimo número armónico.

---

## Verificación empírica

Corriendo 100,000 simulaciones con `n = 8` (`problema3.py`):

```
E[contrataciones] simulado : 2.7178
Hn (valor teórico)         : 2.7179
ln(n) ≈                    : 2.0794

P(best-case = 1 hire) simulado : 0.1250
P(best-case) teórico = 1/n     : 0.1250

P(worst-case = n hires) simulado : 0.000000
P(worst-case) teórico = 1/n!     : 0.000025
```

El worst-case es tan improbable que en 100,000 ensayos prácticamente no aparece.

---

## Código

Ver implementación completa en Python: [`problema3.py`](./problema3.py)