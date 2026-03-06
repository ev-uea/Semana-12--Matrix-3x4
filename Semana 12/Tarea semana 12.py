asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("--- Reservación de Asientos ---")
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

if 0 <= f <= 2 and 0 <= c <= 3:
    asientos[f][c] = 1
    print(f"\n¡Asiento [{f}][{c}] reservado con éxito!")
else:
    print("\nError: Posición fuera de rango.")

print("\nEstado actual de la sala:")
print("---------------------------")
for i in range(3):        # Bucle para filas
    for j in range(4):    # Bucle para columnas
        print(asientos[i][j], end=" ")  # 'end=" "' evita el salto de línea
    print()  # Salto de línea al terminar cada fila
print("---------------------------")