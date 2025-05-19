#Escribe un programa que pida al usuario que ingrese una letra del alfabeto y determine si es una vocal o una consonante.
letra = str (input("ingrese una sola letra: " ))
if letra in "aeiou":
    print ("es una vocal")
else:
    print ("es una consonate")
