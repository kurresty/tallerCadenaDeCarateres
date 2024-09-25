mensaje = "Punto 1 "
textCenter  = mensaje.center(100, "_")
print(textCenter)
name = "Luis"
age = 27
favouriteFood = "Pasta con salsa Boloñesa"
presentacion = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(presentacion)


mensaje = "Punto 2 "
textCenter  = mensaje.center(100, "_")
print(textCenter)
nombre = input("Hola ingresa tu nombre completo: ")
contarNombre = len(nombre.replace(" ", ""))
saludo = f"Hola, {nombre}! Tu nombre tiene {contarNombre} letras"
print(saludo)


mensaje = "Punto 3 "
textCenter  = mensaje.center(100, "_")
print(textCenter)
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
mensaje = (f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y "
           f"los ingresos crecieron un {revenueGrowthPercent:.2f}%.")
print(mensaje)


mensaje = "Punto 4 "
textCenter  = mensaje.center(100, "_")
print(textCenter)
secretMessage = "aS!Ir waQm VL!eDafrcnXi n=gS .P,yytahgoln.!"
omitirCarac= secretMessage[3:]
indices = [0, 2, 4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23,25, 27,29, 31, 33, 35,37 , 39]
# Crear el mensaje decodificado a partir de los indices
omitirCarac = ''.join(omitirCarac[i] for i in indices)
print(omitirCarac)



mensaje = "Punto 5 "
textCenter  = mensaje.center(100, "_")
print(textCenter)
text = 'El nombre "Python" viene dado por la afición de Van Rossum al grupo Monty Python.'
numeroPalabras = len(text.split())
print(f"Numero de palabras en la frase: {numeroPalabras}")



mensaje = "Punto 6 "
textCenter  = mensaje.center(100, "_")
print(textCenter)
word = "Camila"
reemplazarletra = word.replace('a', 'e')
print(reemplazarletra)



mensaje = "Punto 7"
textCenter  = mensaje.center(100, "_")
print(textCenter)
frase = "La historia del lenguaje de programación Python".split()
palabrasInvertidas = reversed(frase)
fraseInvertida= ' '.join(palabrasInvertidas)
print(fraseInvertida)