#Escribe un programa que muestre las tablas de multiplicar del 1 al 10.

for i in range(1, 11):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print("-" * 20)
