# Problema 7b: Fun-Sort y Verificación del Teorema 6

## Enunciado

Implementar el algoritmo **Fun-Sort** y verificar su complejidad asintótica bajo diferentes escenarios:

**Teorema 6**: Si $F = o\left(\frac{n^2}{\log n}\right)$, entonces Fun-Sort corre en tiempo $O(n \log n)$.



## Algoritmo

```
función fun_sort(A):
    n ← len(A)
    comparaciones ← 0
    swaps ← 0
    
    mientras count_inversions(A) > 0:
        para i en 0..n-1:
            x ← A[i]
            l ← -1
            h ← n
            
            // Búsqueda binaria O(log n)
            mientras l + 1 < h:
                m ← ⌊(l + h) / 2⌋
                comparaciones ← comparaciones + 1
                
                si x ≤ A[m]:
                    h ← m
                sino:
                    l ← m
            
            // Reinsertar si está fuera de lugar
            si h < i y A[h] ≠ x:
                intercambiar A[i] ↔ A[h]
                swaps ← swaps + 1
            sino si h > i:
                target ← h - 1
                si target > i y A[target] ≠ x:
                    intercambiar A[i] ↔ A[target]
                    swaps ← swaps + 1
    
    retornar (A, comparaciones, swaps)
```

---


## Análisis de complejidad

El **Teorema 6** establece la regla teórica: Fun-Sort solo corre en $O(n \log n)$ si $F$ crece más lento que $\frac{n^2}{\log n}$ (es decir, $F = o(\frac{n^2}{\log n})$). 

Calculamos esta frontera teórica y la comparamos con nuestro experimento para $n=8$:

* **Umbral del Teorema 6 (límite máximo de F):** $$\frac{n^2}{\log_2 n} = \frac{8^2}{\log_2 8} = \frac{64}{3} \approx 21.33$$

* **Valor esperado de inversiones $E[F]$ (permutación aleatoria):** $$E[F] = \frac{n(n-1)}{4} = \frac{8(7)}{4} = \frac{56}{4} = 14$$


## Verificación Empírica

Aquí comprobamos cómo cambia la velocidad de Fun-Sort dependiendo de qué tan desordenado esté el arreglo al iniciar:

* **Prueba 1: Input casi ordenado** `[1, 2, 3, 4, 5, 6, 7, 8]`
    * **Inversiones (F):** 0
    * **Resultado:** Excelente (**O(n log n)**). Como ya está ordenado, no hace esfuerzo extra y cumple la teoría a la perfección.

* **Prueba 2: Permutación aleatoria** `[3, 1, 4, 1, 5, 9, 2, 6]`
    * **Inversiones (F):** 12
    * **Resultado:** Degradado (**O(n²)**). Al ser un caso típico desordenado, las comparaciones reales se disparan, demostrando que ya no es tan eficiente.

* **Prueba 3: Arreglo invertido** `[8, 7, 6, 5, 4, 3, 2, 1]`
    * **Inversiones (F):** 28 (El peor caso posible)
    * **Resultado:** Muy lento (**O(n² log n)**). El exceso de inversiones hace que el rendimiento caiga drásticamente.

### Conclusión y Comparación
Para el caso específico de $n=8$, el promedio de inversiones en una permutación aleatoria ($14$) parece estar por debajo del umbral exigido ($21.33$).

Sin embargo, esto es una ilusión de los números pequeños. A medida que $n$ crece, la función del caso promedio ($\frac{n^2}{4}$) crece mucho más rápido que la función del umbral ($\frac{n^2}{\log n}$). Por lo tanto, asintóticamente, las permutaciones aleatorias rompen el límite del Teorema 6 y su complejidad se degrada a $O(n^2 \log n)$.


## Referencias al código

- [Implementación: 7b.py](./7b.py)
