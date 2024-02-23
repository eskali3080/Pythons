dineroV = 3
boleto = 0.9

compra = dineroV/boleto 



if compra >= 1 and compra < 2:
    print(f"Puede compra 1 y le sobra: {dineroV - boleto}")

elif compra >= 2 and compra < 3:
    print(f"Puede comprar 2 y le sobra: {dineroV - boleto*2}")

elif compra >=3:
    # Nos ahorramos otra linea de código haciendo la operación directo en el print
    # resultado = str(dineroV - boleto*3)
    print(f"Puede comprar y le sobra: {dineroV - boleto*3}")

else: print("No compra nada")
    
    
    