## Explicación de la fórmula

Sea ( I_k ) el evento:
“se necesitan al menos ( k ) comparaciones para verificar el orden”.

Esto implica que **las primeras ( k ) comparaciones no detectan ninguna inversión**, es decir, todos los pares comparados hasta ese punto están en el orden correcto.

Para que el algoritmo alcance la comparación ( k ), es necesario que los primeros ( k ) elementos de la permutación estén en orden creciente.

### Probabilidad del evento

Consideremos los primeros ( k ) elementos de una permutación uniforme aleatoria:

* Existen ( k! ) posibles ordenaciones de esos ( k ) elementos.
* Todas las ordenaciones son igualmente probables.
* Solo una de ellas está completamente ordenada de forma creciente.

Por lo tanto:

[
P(\text{los primeros } k \text{ elementos están ordenados}) = \frac{1}{k!}
]

---

El evento ( I_k ) ocurre si y solo si:

* Ninguna de las primeras ( k ) comparaciones detecta una inversión.
* Esto equivale a que los primeros ( k ) elementos estén en orden creciente.

Por lo tanto:

[
P(I_k) = \frac{1}{k!}
]

