def tablas_de_multiplicar(numero):
    for i in range(1, 101):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número para ver sus tablas de multiplicar del 1 al 100: "))

tablas_de_multiplicar(numero)
