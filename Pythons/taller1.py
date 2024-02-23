# nombre = "Nicolas"
# apellido = "Tarazona"
# celular = "3222641983" 

# print(nombre + " " + apellido + " " + celular)
# print(f"{nombre} {apellido} {celular}")
# print("Hola me llamo {} {} y mi celular es: {}".format(nombre,apellido,celular))


# cadena = "Hola Mundo"
# print(type(cadena))

# entero = 99
# print(type(entero))

# flotante = 4.2 
# print(type(flotante))

# booleano = True
# print(type(booleano))

# cadena = "Hola Mundo"
# print(cadena)

# entero = 99
# print(entero)

# flotante = 4.2 
# print(flotante)

# booleano = True
# print(booleano)


# lista = [10, 20, 30, 100, 200]
# print(lista[2])
# print(lista)
# print(type(lista))

# listaString = [44, "treinta", 30, "cuarenta"]
# print(listaString)
# print(type(listaString))

# tuplanocambia = ("Curso", "de", "python")
# print(tuplanocambia)
# print(type(tuplanocambia))

# diccionario = {
#     "nombre": "Nicolas",
#     "apellido": "Tarazona",
#     "curso": "python"
# }
# print(diccionario)
# print(type(diccionario))
# print(diccionario["nombre"])

# x = 3
# y= 2
# texto = "Hola Mundo"
# numero = str(x + y)
# print(texto + " " + numero)

# edad = 55
# print(edad)

# # Primera forma de sumar a una variable (manera mas optimizada)
# edad += 5

# # Segunda forma de sumar una variable (no tan optimizada)
# edad = edad + 5

# # Manera optimizada 
# edad -= 5
# print(edad)

# nombre = input("Cual es su nombre?: ")
# edad = int(input("Cual es su edad?: "))

# print("Bienvenido ", nombre, "tienes ", edad, "años" )
# print(f"Bienvenido ",nombre, "en 2026 tendrás ", (edad)+2)

# dineroV = 3
# boleto = 0.9

# compra = dineroV/boleto 



# if compra >= 1 and compra < 2:
#     print(f"Puede compra 1 y le sobra: {dineroV - boleto}")

# elif compra >= 2 and compra < 3:
#     print(f"Puede comprar 2 y le sobra: {dineroV - boleto*2}")

# elif compra >=3:
#     # Nos ahorramos otra linea de código haciendo la operación directo en el print
#     # resultado = str(dineroV - boleto*3)
#     print(f"Puede comprar y le sobra: {dineroV - boleto*3}")

# else: print("No compra nada")

# Proyecto 1 

pregunta = input("¿Nombra tu marca de ropa preferida?")
pregunta2 = input("¿Cual tu actor favorito?")

print("El nombre de tu cerveza sera ", (pregunta[0:2] + pregunta2[0:2]))



