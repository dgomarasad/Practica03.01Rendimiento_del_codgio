#Escribir dos funciones, una función que reciba un número entero positivo n y
#calcule el número de fibonacci asociado a ese número de manera recursiva y
#otra función que haga la misma operación pero con bucles.Con ambas funciones, 
#calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por 
#fuerza bruta.
import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n_values = [1, 10, 20, 30, 40]

for n in n_values:
    start = time.time()
    fib_rec = fibonacci_recursive(n)
    time_rec = time.time() - start

    start = time.time()
    fib_iter = fibonacci_iterative(n)
    time_iter = time.time() - start

    print(f"n={n} | Recursivo: {time_rec:.6f}s, Iterativo: {time_iter:.6f}s")
