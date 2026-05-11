# Analisis Probabilistico de Algoritmos Aleatorizados

Repositorio con soluciones teoricas y verificaciones experimentales en Python para ejercicios de analisis probabilistico de algoritmos aleatorizados.

La idea del proyecto es combinar dos entregables por problema:

- una explicacion en Markdown con el desarrollo matematico
- una implementacion en Python para simular, verificar o ilustrar el resultado teorico

Varios ejercicios, en especial los problemas 6 y 7, toman como referencia el paper Sorting the Slow Way: An Analysis of Perversely Awful Randomized Sorting Algorithms.

## Estructura del repositorio

| Archivo | Descripcion |
|---|---|
| [problema1_solucion.md](./problema1_solucion.md) | Explica como construir un generador uniforme en [a, b] usando solo bits aleatorios justos. |
| [problema1_generador_uniforme.py](./problema1_generador_uniforme.py) | Implementa el generador uniforme y valida empiricamente su distribucion y tiempo esperado. |
| [problema2_solucion.md](./problema2_solucion.md) | Desarrolla el truco de Von Neumann para quitar sesgo a una moneda. |
| [problema2_von_neumann.py](./problema2_von_neumann.py) | Simula el algoritmo de Von Neumann y compara resultados simulados contra valores teoricos. |
| [6b_solucion.md](./6b_solucion.md) | Justifica por que \(E[C] = \sum_{k>0} P[I_k]\) usando suma de colas para variables enteras no negativas. |
| [6b.py](./6b.py) | Calcula el valor teorico de \(E[C]\) y lo compara con simulacion sobre permutaciones aleatorias. |
| [6c_solucion.md](./6c_solucion.md) | Explica por que el numero de iteraciones de bogo-sort sigue una distribucion geometrica. |
| [6c.py](./6c.py) | Simula iteraciones y swaps de bogo-sort con Fisher-Yates para contrastar teoria y experimento. |
| [7a_solucion.md](./7a_solucion.md) | Compara Guess-Sort contra Bozo-Sort+_opt y analiza por que uno desperdicia menos pasos. |
| [7a.py](./7a.py) | Ejecuta ensayos comparativos entre Guess-Sort y Bozo-Sort+_opt. |
| [7b_solucion.md](./7b_solucion.md) | Describe Fun-Sort y discute el Teorema 6 segun el numero de inversiones iniciales. |
| [7b.py](./7b.py) | Implementa Fun-Sort y realiza pruebas para observar su comportamiento experimental. |

## Requisitos

- Python 3.9 o superior
- No se requieren dependencias externas; todos los scripts usan la libreria estandar

## Como ejecutar

Desde la raiz del repositorio:

```bash
python problema1_generador_uniforme.py
python problema2_von_neumann.py
python 6b.py
python 6c.py
python 7a.py
python 7b.py
```

En PowerShell tambien puedes ejecutarlos con:

```powershell
python .\problema1_generador_uniforme.py
python .\problema2_von_neumann.py
python .\6b.py
python .\6c.py
python .\7a.py
python .\7b.py
```

## Que muestra cada script

- Problema 1: uniformidad aproximada de la salida, numero esperado de intentos y relacion con rechazo de valores fuera de rango.
- Problema 2: salida aproximadamente 50/50 para distintos valores de \(p\) y comparacion entre costo teorico y costo simulado.
- Problema 6b: suma de probabilidades \(1/k!\), aproximacion a \(e - 1\) y contraste con simulacion.
- Problema 6c: comportamiento geometrico del numero de iteraciones de bogo-sort y costo esperado en swaps.
- Problema 7a: comparacion experimental entre pasos desperdiciados e intercambios utiles.
- Problema 7b: pruebas de Fun-Sort en casos ordenados, aleatorios e invertidos, junto con el analisis del numero de inversiones.

## Enfoque del repositorio

Este repositorio esta orientado a documentar el razonamiento probabilistico detras de cada ejercicio, no solo a mostrar codigo. Por eso la lectura recomendada es:

1. Revisar primero el archivo de solucion en Markdown.
2. Ejecutar luego el script en Python correspondiente.
3. Comparar la intuicion teorica con la evidencia experimental.

## Referencia principal

- Gruber, H., Holzer, M., y Ruepp, O. Sorting the Slow Way: An Analysis of Perversely Awful Randomized Sorting Algorithms. FUN 2007.