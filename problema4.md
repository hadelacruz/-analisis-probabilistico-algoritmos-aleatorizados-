# Problema 4: Suma esperada de n dados

## Enunciado

Usar variables aleatorias para calcular la suma esperada de `n` dados lanzados a la vez.

---

## Idea central

Sea $X = X_1 + X_2 + \cdots + X_n$ donde $X_i$ es el valor del dado $i$. Por **linealidad de la esperanza**:

$$E[X] = E[X_1] + E[X_2] + \cdots + E[X_n] = n \cdot E[X_1]$$

Solo necesitamos calcular la esperanza de un dado individual.

---

## Esperanza de un dado

Cada cara tiene probabilidad $1/6$, entonces:

$$E[X_1] = \frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5$$

Por lo tanto:

$$E[X] = 3.5n$$

---

## Enfoque con variables indicadoras

Definimos $Y_{ij} = 1$ si el dado $i$ muestra la cara $j$, y 0 si no. Entonces:

$$X_i = \sum_{j=1}^{6} j \cdot Y_{ij}$$

Como $E[Y_{ij}] = P(Y_{ij} = 1) = 1/6$, por linealidad:

$$E[X_i] = \sum_{j=1}^{6} j \cdot \frac{1}{6} = 3.5$$

El resultado es el mismo, pero el enfoque de indicadoras es más formal y generalizable.

---

## Por qué es poderosa la linealidad

Lo clave es que la linealidad de la esperanza **no requiere independencia**. Aunque los dados fueran dependientes entre sí (lo cual sería raro, pero posible en otros problemas), el resultado seguiría siendo $3.5n$. No necesitamos conocer la distribución conjunta de todos los dados — solo la esperanza de cada uno por separado.

---

## Verificación empírica

Corriendo 20,000 simulaciones con `problema4.py`:

```
    n |  Teórico |   Simulado
------------------------------
    1 |      3.5 |      3.499
    2 |      7.0 |      6.999
    5 |     17.5 |     17.508
   10 |     35.0 |     35.023
   20 |     70.0 |     69.940
  100 |    350.0 |    350.083
```

El simulado converge al teórico en todos los casos.

---

## Código

Ver implementación completa en Python: [`problema4.py`](./problema4.py)