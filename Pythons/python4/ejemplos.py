# print("Ejemplo 1")

# def muestraNombre():
#     print("Victor")
#     print("Paco")
#     print("Juan")
#     print("Francisco")
#     print("Aitor")
#     print("Nestor")
#     print("\n")

# muestraNombre()


# print("Ejemplo 2")

# def mostrarTuNombre(nombre):
#     print(f"Tu nombre es: {nombre}")

# nombre = input("Ingresa tu nombre: ")
# mostrarTuNombre(nombre)



# print("Ejemplo 2.1")

# def mostrarTuNombre(nombre, edad):
#     print(f"Tu nombre es: {nombre}")

#     if edad >= 18:
#         print("Y eres mayor de edad")

# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# mostrarTuNombre(nombre, edad)


# print("Ejemplo 3")

# def tabla(numero):
#     print(f"Tabla de multiplicar del numero: {numero}")

#     for contador in range(11):
#         operacion = numero*contador
#         print(f"{numero} x {contador} = {operacion}")

# tabla(3)


# print("Ejemplo 4")

# def getEmpleado(nombre, dni = None):
#     print("EMPLEADO")
#     print(f"Nombre: {nombre}")

#     if dni != None:
#         print(f"DNI: {dni}")

# getEmpleado("Victor Robles WEB", 355252)


# print("Ejemplo 5")

# def saludame(nombre):
#     saludo = f"Hola, saludos {nombre}"
#     return saludo

# print(saludame("Darwin Celis"))


# print("Ejemplo 6")

# def calculadora(numero1, numero2, basicas = False):

#     suma = numero1+numero2
#     resta = numero1-numero2
#     multi = numero1*numero2
#     division = numero1/numero2

#     cadena = " "

#     if basicas != False:
#         cadena += "Suma: " + str(suma)
#         cadena += "\n"
#         cadena += "Resta: " + str(resta)
#         cadena += "\n"
#     else: 
#         cadena += "Multiplicacion: " + str(multi)
#         cadena += "\n"
#         cadena += "Division: " + str(division)

#     return cadena
# print(calculadora(56,5, True))


# print("Ejemplo 7")

# def getNombre(nombre):
#     texto = f"El nombre es: {nombre}"
#     return texto

# def getApellidos(apellidos):
#     texto = f"Los apellidos son: {apellidos}"
#     return texto

# def devuelveTodo(nombre, apellidos):
#     texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
#     return texto

# print(devuelveTodo("Victor", "Robles"))


# print("Ejemplo 8")

# dime_el_year = lambda year: f"El año es {year}"

# print(dime_el_year(2024))


# print("ejemplo variable global")

# frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"

# print(frase)

# def holamundo():
#     frase = " Hola Mundo!!"
#     print(frase)

#     year = 2024
#     print(year)

#     global website
#     website = "sena.edu.co"
#     print(" Dentro : ", website)
#     return year
# print(holamundo())
# print("Fuera:", website)



# print("Funciones predefinidas")
# nombre = "Victor Robles"

# print(type(nombre))

# comprobar = isinstance(nombre, str)
# if comprobar: 
#     print("Esa variables es un string")
# else: 
#     print("No es una cadena")

# if not isinstance(nombre, float):
#     print("La variable no es un numero con decimales")



#limpiar espacios

# frase = "   mi contenido   "
# print(frase)
# print(frase.strip())


#comprobar variable vacía

# texto = " ff "

# if len(texto) <= 0:
#     print("la variable esta vacía")
# else:
#     print("La variable tiene contenido: ", len(texto))


#Eliminar variables
# year = 2024
# print(year)
# del year

#print(year)


# #Encontrar caracteres
# frase = "La vida es bella"
# print(frase.find("vida"))
# # Reemplazar palabras en un string
# nueva_frase = frase.replace("vida", "moto")
# print(nueva_frase)


# Mayúsculas y minúsculas
# nombre = "Marco"
# print(nombre)
# print(nombre.lower())
# print(nombre.upper())


def mi_funcion(nombre):
    return "Hola que tal " + nombre

def mi_segunda_funcion(apellidos):
    return "Hola que tal 2" + apellidos


nombre = "Victor" 
apellidos = "Robles"

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellidos))























