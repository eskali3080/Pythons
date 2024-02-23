# Input 1
# Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:
# ¿Qué estás estudiando?

estudio = input("¿Que estas estudiando?")
print("Estas estudiando: ", estudio)

# Input 2
# Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:
# ¿En qué país vives?

pais = input("¿En que país vives?")
print("Vives en ", pais)

# Input 3
# Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su
# nombre y apellido con las siguientes instrucciones:
# Escribe tu nombre:
# Escribe tu apellido:
# El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio.

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
print(nombre + " " + apellido)

# Proyecto 1 

pregunta = input("¿Nombra tu marca de ropa preferida?")
pregunta2 = input("¿Cual tu actor favorito?")

print("El nombre de tu cerveza sera ", (pregunta[0:2] + pregunta2[0:2]))