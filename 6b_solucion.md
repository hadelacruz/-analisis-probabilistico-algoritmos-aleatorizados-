# Problema 6b: Por que E[C] = suma P[I_k]

## Enunciado

En la prueba del Teorema 2, explique por que:

$$
E[C] = \sum_{k>0} P[I_k]
$$

---

## Idea central

`C` es una variable aleatoria entera no negativa: cuenta cuantas comparaciones hace la subrutina `sorted` antes de detenerse.

Para una variable aleatoria entera no negativa se cumple la identidad de suma de colas:

$$
E[C] = \sum_{k \ge 1} P(C \ge k)
$$

En el paper, `I_k` es precisamente el evento equivalente a:

$$
C \ge k
$$

Por eso:

$$
E[C] = \sum_{k>0} P(C \ge k) = \sum_{k>0} P[I_k]
$$

---

## Demostracion de la identidad

Para cualquier valor concreto `C = c`, se puede escribir:

$$
c =
\mathbf{1}_{c \ge 1}
+ \mathbf{1}_{c \ge 2}
+ \mathbf{1}_{c \ge 3}
+ \cdots
$$

Si `c = 4`, por ejemplo:

$$
4 = 1 + 1 + 1 + 1 + 0 + 0 + \cdots
$$

Entonces, como variable aleatoria:

$$
C = \sum_{k \ge 1} \mathbf{1}_{C \ge k}
$$

Aplicando esperanza y linealidad:

$$
E[C]
= E\left[\sum_{k \ge 1} \mathbf{1}_{C \ge k}\right]
= \sum_{k \ge 1} E[\mathbf{1}_{C \ge k}]
$$

La esperanza de un indicador es la probabilidad del evento:

$$
E[\mathbf{1}_{C \ge k}] = P(C \ge k)
$$

Por lo tanto:

$$
E[C] = \sum_{k \ge 1} P(C \ge k)
$$

Y como `I_k` equivale a `C >= k`:

$$
E[C] = \sum_{k>0} P[I_k]
$$

---

## Aplicacion al Teorema 2

Del inciso 6a:

$$
P[I_k] = \frac{1}{k!}
$$

Como el algoritmo puede hacer a lo mas `n-1` comparaciones, la suma finita es:

$$
E[C] =
\sum_{k=1}^{n-1} \frac{1}{k!}
$$

Cuando `n` crece, esta suma se acerca a:

$$
\sum_{k=1}^{\infty} \frac{1}{k!}
=
\left(\sum_{k=0}^{\infty} \frac{1}{k!}\right) - 1
= e - 1
\approx 1.71828
$$

Esto explica por que, aunque en el peor caso verificar si un arreglo esta ordenado cuesta `n-1` comparaciones, para una permutacion aleatoria el numero esperado de comparaciones es casi constante.

---

## Verificacion numerica

La implementacion en Python [`6b.py`](./6b.py) calcula:

```text
E[C] = sum_{k=1}^{n-1} 1/k!
```

y tambien simula permutaciones aleatorias para confirmar que el promedio experimental se acerca al valor teorico.

Salida esperada aproximada para `n = 10`:

```text
E[C] teorico para n=10: 1.718282
Limite e - 1:            1.718282
Simulacion:              cerca de 1.72
```

---

## Video

Pendiente: agregar aqui el enlace del video de YouTube no listado del grupo.

---

## Referencias

- Hermann Gruber, Markus Holzer y Oliver Ruepp. *Sorting the Slow Way: An Analysis of Perversely Awful Randomized Sorting Algorithms*. FUN 2007. PDF consultado: https://archivedsite.air.in.tum.de/Main/Publications/Ruepp2007.pdf
- Parte de esta redaccion y el codigo de verificacion fueron generados con apoyo de Codex (OpenAI) y deben ser revisados y comprendidos por el grupo antes de entregarlos.
