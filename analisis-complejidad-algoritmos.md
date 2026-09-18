# Análisis de Complejidad — Anidada vs Binaria vs Hash

## Datos reales obtenidos

| N | Anidada (ms) | Binaria (ms) | Hash (ms) |
|---|---|---|---|
| 100 | 0.1638 | 0.0559 | 0.0039 |
| 1,000 | 15.3657 | 0.8458 | 0.0321 |
| 10,000 | 1,496.9740 | 12.9389 | 0.3699 |

## Complejidad de cada algoritmo

| Algoritmo | Complejidad | Comportamiento al multiplicar N por 10 |
|---|---|---|
| Anidada | O(n²) | El tiempo se multiplica por **100** (10²) |
| Binaria | O(n log n) | El tiempo se multiplica por **~12.5** |
| Hash | O(n) | El tiempo se multiplica por **10** |

Esto se confirma con los datos reales: de N=1,000 a N=10,000, la Anidada pasó de 15.37 ms a 1,496.97 ms (×97, ≈×100), mientras que Binaria y Hash escalan mucho más suavemente.

## Metodología de extrapolación

Para estimar tiempos con N mayores a los medidos, se aplica el factor de crecimiento teórico de cada complejidad sobre el último dato real (N=10,000):

- **O(n²):** factor = (N_nuevo / N_base)²
- **O(n):** factor = N_nuevo / N_base
- **O(n log n):** factor = (N_nuevo · log N_nuevo) / (N_base · log N_base)

## Estimación para N = 100,000 (×10 respecto a N=10,000)

| Algoritmo | Cálculo | Tiempo estimado |
|---|---|---|
| Anidada | 1,496.9740 ms × 10² | **≈ 149.7 s (~2.5 min)** |
| Binaria | 12.9389 ms × 12.5 | **≈ 161.7 ms (~0.16 s)** |
| Hash | 0.3699 ms × 10 | **≈ 3.7 ms** |

## Estimación para N = 1,000,000 (×100 respecto a N=10,000)

| Algoritmo | Cálculo | Tiempo estimado |
|---|---|---|
| Anidada | 1,496.9740 ms × 100² | **≈ 14,970 s (~4.2 horas)** |
| Binaria | 12.9389 ms × ~166 | **≈ 2.15 s** |
| Hash | 0.3699 ms × 100 | **≈ 37 ms** |

## Conclusión

- La versión **Anidada (O(n²))** es manejable hasta N≈10,000-100,000, pero se vuelve completamente inviable a partir de N≈1,000,000 (horas de ejecución).
- **Binaria (O(n log n))** y **Hash (O(n))** escalan de forma mucho más eficiente y siguen siendo prácticas incluso con millones de elementos.
- Esto ilustra por qué, en la práctica, se evita el enfoque de fuerza bruta (anidado) para datasets grandes, prefiriendo estructuras de búsqueda binaria o tablas hash.
