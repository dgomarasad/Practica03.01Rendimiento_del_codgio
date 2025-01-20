#Escribir dos funciones, una función que reciba un número entero positivo n y
#calcule el número de fibonacci asociado a ese número de manera recursiva y
#otra función que haga la misma operación pero con bucles.Con ambas funciones, 
#calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por 
#fuerza bruta.
import time

# Lista de valores de n
valores_n = [1, 10, 20, 30, 40]

# Función para medir el tiempo de ejecución
def medir_tiempo(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

# Comparación de tiempos para cada n
for n in valores_n:
    print(f"n = {n}")
    
    # Medir tiempo de la función recursiva
    tiempo_recursivo = medir_tiempo("fibonacci_recursivo", n)
    print(f"Tiempo (recursivo) para n={n}: {tiempo_recursivo:.6f} segundos")
    
    # Medir tiempo de la función iterativa
    tiempo_iterativo = medir_tiempo("fibonacci_iterativo", n)
    print(f"Tiempo (iterativo) para n={n}: {tiempo_iterativo:.6f} segundos")
    
    print("-" * 50)
