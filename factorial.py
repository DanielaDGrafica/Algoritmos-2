def factorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado


numero = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es {resultado_factorial}")