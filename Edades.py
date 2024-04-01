def calcular_rango_edades(edad):
    if edad <= 20:
        return "0-20"
    elif edad <= 30:
        return "20-30"
    elif edad <= 40:
        return "30-40"
    elif edad <= 60:
        return "40-60"
    else:
        return "mayores de 60"

rangos_edades = {
    "0-20": 0,
    "20-30": 0,
    "30-40": 0,
    "40-60": 0,
    "mayores de 60": 0
}

for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
    rango = calcular_rango_edades(edad)
    rangos_edades[rango] += 1

print("\nTotal de personas por rango de edades:")
for rango, total in rangos_edades.items():
    print(f"{rango}: {total}")