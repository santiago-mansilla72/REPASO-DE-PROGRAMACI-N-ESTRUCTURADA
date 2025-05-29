#Escribe un programa que pida al usuario que ingrese un número y luego muestre la suma de los números impares desde 1 hasta ese número.
num = int(input("ingresa un numero: "))

suma = 0
for i in range(1, num + 1):
    if i % 2 !=0:
        suma += i
print(f"La suma de los números impares desde 1 hasta {num} es: {suma}")
