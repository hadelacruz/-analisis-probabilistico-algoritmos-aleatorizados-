## Número esperado de inversiones en una permutación aleatoria

Sea ( A ) una permutación aleatoria de los números ( [1, \dots, n] ).
Una inversión es un par ( (i, j) ) tal que ( i < j ) y ( A[i] > A[j] ).

---

### 1. Variables indicadoras

Definimos una variable aleatoria indicadora para cada par ( (i,j) ):

[
X_{ij} =
\begin{cases}
1 & \text{si } A[i] > A[j] \
0 & \text{en otro caso}
\end{cases}
]

Entonces, el número total de inversiones es:

[
X = \sum_{i<j} X_{ij}
]

### 2. Esperanza del número de inversiones

Por linealidad de la esperanza:

[
E[X] = \sum_{i<j} E[X_{ij}]
]

Ahora, para cualquier par ( (i,j) ), como la permutación es aleatoria:

* Es igualmente probable que ( A[i] > A[j] ) o ( A[i] < A[j] )

Por lo tanto:

[
P(A[i] > A[j]) = \tfrac{1}{2}
]

y entonces:

[
E[X_{ij}] = \tfrac{1}{2}
]

### 3. Número de pares

El número de pares ( (i,j) ) con ( i < j ) es:

[
\binom{n}{2} = \frac{n(n-1)}{2}
]

### 4. Resultado final

Sustituyendo:

[
E[X] = \frac{n(n-1)}{2} \cdot \frac{1}{2} = \frac{n(n-1)}{4}
]
