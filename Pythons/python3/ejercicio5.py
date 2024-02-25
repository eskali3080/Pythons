numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrse el segundo numero: "))

if numero1 < numero2: 

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else: 
    print("El primer numero debe ser menor que el segundo numero")