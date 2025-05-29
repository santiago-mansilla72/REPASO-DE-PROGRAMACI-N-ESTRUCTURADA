#Escribe un programa que pida al usuario que ingrese números enteros positivos y luego calcule la suma de todos los números ingresados hasta que el usuario ingrese un número negativo.

suma = 0
numeros = 0
while numeros >= 0:
    numeros = int(input("Ingrese un numero entero:"))
    if numeros > 0:
        suma += numeros
print (f"la suma de los numeros es: {suma}")
