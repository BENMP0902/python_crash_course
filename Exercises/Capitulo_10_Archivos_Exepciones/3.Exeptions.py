# Booque 3: Exepciones (10-6 a 10-10)
# Las exepciones evitan que el programa se detenga bruscamente (crashe) ante un error.
# Calculadora de Sumas:
print("Introduce dos números para realizar una suma")
print("Escribe 'q' para salir :)")

while True:
    try:
        num1 = input("Primer número: ")
        if num1 == 'q':
            break
        num2 = input("Segundo número: ")
        if num2 == 'q':
            break
        
        resultado = int(num1) + int(num2)

    except ValueError:
        print("Solo se permiten números enteros.")
    else:
        print(f"El resltado de la suma es:{resultado}")

