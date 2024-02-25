contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int(input("¿Cuantos aprendices tienes?: "))


while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quiere ponerle al aprendiz {contador}?: "))

    if nota >= 3:
        aprobados += 1
    else: 
        reprobados += 1

    contador += 1

print(f"Aprendices Aprobados: {aprobados}")
print(f"Aprendices Reprobados: {reprobados}")