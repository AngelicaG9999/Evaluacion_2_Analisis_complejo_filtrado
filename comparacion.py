import time
import random
import statistics
import matplotlib.pyplot as plt


# Busqueda anidada O(n^2)
def busqueda_anidada(a, b):
    resultado = []

    for elemento_a in a:
        for elemento_b in b:
            if elemento_a == elemento_b:
                resultado.append(elemento_a)
                break

    return resultado


# Busqueda binaria
def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == valor:
            return True

        if lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return False


#Ordenar B y buscar cada elemento usando busqueda binaria O(n log n)
def interseccion_binaria(a, b):
    b_ordenado = sorted(b)
    resultado = []

    for elemento in a:
        if busqueda_binaria(b_ordenado, elemento):
            resultado.append(elemento)

    return resultado


# Usar un set O(n)
def interseccion_hash(a, b):
    conjunto_b = set(b)
    resultado = []

    for elemento in a:
        if elemento in conjunto_b:
            resultado.append(elemento)

    return resultado


# Genero dos listas sin elementos en comun para que la interacción anidada a recorra completamente la segunda lista.
def generar_peor_caso(n):
    a = list(range(n))
    b = list(range(n, n * 2))

    random.Random(2026 + n).shuffle(b)

    return a, b


# Medir el tiempo de ejecucion de cada metodo
def medir_tiempo(funcion, a, b, repeticiones=7):
    tiempos = []

    for i in range(repeticiones):
        inicio = time.perf_counter_ns()

        funcion(a, b)

        fin = time.perf_counter_ns()

        tiempo = (fin - inicio) / 1_000_000
        tiempos.append(tiempo)

    # Uso la mediana para evitar que un valor muy alto o muy bajo afecte demasiado el resultado
    return statistics.median(tiempos)


def ejecutar_comparaciones():
    tamanios = [100, 1000, 10000]

    # Se quita el 100000, porque tarda demasiado en ejecutarse y no es necesario para ver la tendencia de los algoritmos

    tiempos_anidada = []
    tiempos_binaria = []
    tiempos_hash = []

    print("\nRESULTADOS")
    print("-" * 70)

    print(
        f"{'N':<10}"
        f"{'Anidada (ms)':<20}"
        f"{'Binaria (ms)':<20}"
        f"{'Hash (ms)':<20}"
    )

    print("-" * 70)

    for n in tamanios:
        a, b = generar_peor_caso(n)

        tiempo_anidada = medir_tiempo(busqueda_anidada, a, b)
        tiempo_binaria = medir_tiempo(interseccion_binaria, a, b)
        tiempo_hash = medir_tiempo(interseccion_hash, a, b)

        tiempos_anidada.append(tiempo_anidada)
        tiempos_binaria.append(tiempo_binaria)
        tiempos_hash.append(tiempo_hash)

        print(
            f"{n:<10}"
            f"{tiempo_anidada:<20.6f}"
            f"{tiempo_binaria:<20.6f}"
            f"{tiempo_hash:<20.6f}"
        )

    # Grafica para comparar los tiempos
    plt.figure(figsize=(10, 6))

    plt.plot( tamanios,tiempos_anidada,marker="o",label="Anidada O(n^2)")
    plt.plot(tamanios,tiempos_binaria,marker="o",label="Binaria O(n log n)")
    plt.plot(tamanios,tiempos_hash,marker="o",label="Hash O(n)")

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Tamaño del arreglo (N)")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.title("Comparación de algoritmos de intersección")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()


# Identificar el N* exacto donde la Búsqueda Binaria desplaza al método anidado 
def encontrar_n_asterisco(limite=5000, repeticiones=31):
    n = 2
    n_anterior = 1

    while n <= limite:
        a, b = generar_peor_caso(n)

        tiempo_anidada = medir_tiempo(
            busqueda_anidada,
            a,
            b,
            repeticiones
        )

        tiempo_binaria = medir_tiempo(
            interseccion_binaria,
            a,
            b,
            repeticiones
        )

        # Si la binaria ya es mas rápida, buscamos en donde ocurre el cambio
        if tiempo_binaria < tiempo_anidada:

            inicio = n_anterior + 1

            if inicio < 2:
                inicio = 2

            for candidato in range(inicio, n + 1):
                a, b = generar_peor_caso(candidato)

                tiempo_a = medir_tiempo(busqueda_anidada,a,b,repeticiones)
                tiempo_b = medir_tiempo(interseccion_binaria,a,b,repeticiones)

                if tiempo_b < tiempo_a:
                    return candidato, tiempo_a, tiempo_b

        n_anterior = n
        n = n * 2

    return None


def main():
    ejecutar_comparaciones()

    print("\nBuscando N*...\n")

    resultado = encontrar_n_asterisco()

    if resultado is not None:
        n_estrella, tiempo_anidada, tiempo_binaria = resultado

        print("N* encontrado:", n_estrella)
        print("Tiempo método anidado:", tiempo_anidada, "ms")
        print("Tiempo búsqueda binaria:", tiempo_binaria, "ms")

    else:
        print("No se encontró un N* dentro del límite.")


main()