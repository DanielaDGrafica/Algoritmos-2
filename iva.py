def calcular_precio_con_iva(precio_sin_iva):
    iva = 0.16  # Porcentaje de IVA (16%)
    precio_con_iva = precio_sin_iva * (1 + iva)
    return precio_con_iva

costo_total_sin_iva = 0
for i in range(1, 11):
    precio = float(input(f"Ingrese el costo del producto {i}: "))
    costo_total_sin_iva += precio

costo_total_con_iva = calcular_precio_con_iva(costo_total_sin_iva)

print("\nResumen de la compra:")
print(f"Precio total antes de IVA: ${costo_total_sin_iva:.2f}")
print(f"Precio total después de IVA: ${costo_total_con_iva:.2f}")