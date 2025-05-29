#Escribe un programa que pida al usuario que ingrese una cadena de texto y luego cuente cuántas veces aparece una letra específica en la cadena.
while True:
    texto = input("Ingresa una cadena de texto (o presiona Enter para salir): ")

    if texto == "":
        print("Programa finalizado.")
        break  

    letra = input("Ingresa la letra que quieres contar: ")

    else len(letra) != 1:
        print("Por favor, ingresa solo una letra.")
        continue  

    cantidad = texto.count(letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en la cadena.\n")
