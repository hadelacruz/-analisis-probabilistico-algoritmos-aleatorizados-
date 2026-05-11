# Problema 6c: Iteraciones de bogo-sort

## Enunciado

En la seccion 2.3 del paper *Sorting the Slow Way*, explique por que la variable aleatoria `I`, que cuenta el numero de iteraciones del algoritmo, tiene distribucion geometrica.

---

## Idea central

Bogo-sort funciona repitiendo el mismo experimento:

1. Barajar el arreglo aleatoriamente.
2. Revisar si quedo ordenado.
3. Si no quedo ordenado, volver a intentarlo.

Si los `n` elementos son distintos, existen:

$$
n!
$$

permutaciones posibles. De todas ellas, solamente una esta ordenada de forma creciente.

Por lo tanto, cada barajado tiene probabilidad de exito:

$$
p = P(\text{barajado ordenado}) = \frac{1}{n!}
$$

---

## Por que es geometrica

La variable `I` cuenta cuantos intentos se necesitan hasta obtener el primer barajado ordenado.

Cada intento puede verse como un ensayo de Bernoulli:

```text
exito  = el arreglo queda ordenado
fracaso = el arreglo no queda ordenado
```

Ademas:

- La probabilidad de exito en cada intento siempre es la misma: `p = 1/n!`.
- Los intentos son independientes, porque cada nuevo shuffle vuelve a generar una permutacion uniforme sin depender del historial.
- El algoritmo se detiene en el primer exito.

Esa es exactamente la definicion de una variable aleatoria geometrica.

Entonces:

$$
I \sim \operatorname{Geom}\left(\frac{1}{n!}\right)
$$

---

## Funcion de probabilidad

Para que `I = k`, deben pasar dos cosas:

1. Los primeros `k-1` intentos fallan.
2. El intento `k` tiene exito.

Como cada intento es independiente:

$$
P(I = k)
= (1-p)^{k-1}p
$$

Sustituyendo `p = 1/n!`:

$$
P(I = k)
= \left(1-\frac{1}{n!}\right)^{k-1}
\left(\frac{1}{n!}\right)
$$

para `k = 1, 2, 3, ...`.

---

## Esperanza

Si:

$$
I \sim \operatorname{Geom}(p)
$$

entonces:

$$
E[I] = \frac{1}{p}
$$

Como `p = 1/n!`, se obtiene:

$$
E[I] = n!
$$

Esto significa que bogo-sort necesita, en promedio, `n!` barajados para encontrar la permutacion ordenada.

---

## Numero esperado de swaps

Si el shuffle se implementa con Fisher-Yates, cada barajado hace exactamente `n-1` swaps.

Sea `S` la variable aleatoria que cuenta el numero total de swaps. Como cada iteracion hace `n-1` swaps:

$$
S = (n-1)I
$$

Por linealidad de la esperanza:

$$
E[S] = E[(n-1)I] = (n-1)E[I]
$$

Sustituyendo `E[I] = n!`:

$$
E[S] = (n-1)n!
$$

Por ejemplo, para `n = 4`:

$$
E[I] = 4! = 24
$$

$$
E[S] = (4-1)4! = 3 \cdot 24 = 72
$$

---

## Caso especial: arreglo ya ordenado

El paper aclara que, si la entrada ya esta ordenada, bogo-sort termina inmediatamente y el numero de iteraciones es `0`.

El analisis geometrico se usa para el caso en que el arreglo inicial no esta ordenado. En ese caso, el algoritmo debe empezar a barajar hasta encontrar por primera vez la permutacion correcta.

---

## Verificacion empirica

La implementacion en Python [`6c.py`](./6c.py) simula bogo-sort usando Fisher-Yates y confirma que, para `n = 4`:

```text
E[I] teorico       = 24
E[swaps] teorico   = 72
E[I] simulado      ≈ 24
E[swaps] simulado  ≈ 72
```

---

## Video

Pendiente: agregar aqui el enlace del video de YouTube no listado del grupo.

---

## Referencias

- Gruber, H., Holzer, M., & Ruepp, O. (2007). *Sorting the Slow Way: An Analysis of Perversely Awful Randomized Sorting Algorithms*. FUN 2007, pp. 183-197. PDF consultado: https://archivedsite.air.in.tum.de/Main/Publications/Ruepp2007.pdf
- Mitzenmacher, M., & Upfal, E. (2005). *Probability and Computing: Randomized Algorithms and Probabilistic Analysis*. Cambridge University Press.
- Pitman, J. (1997). *Probability*. Springer-Verlag.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
- Parte de esta redaccion y el codigo de verificacion fueron generados con apoyo de Codex (OpenAI) y deben ser revisados y comprendidos por el grupo antes de entregarlos.
