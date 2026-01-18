# Aqui trabajaremos con dos ideas fundamentales que siempre aparecen juntas en software real:
# 1. Entrada de usuario(input)
# 2. Ejecucuion repetitiva controlada(while)

# Bloque 1: Input y Números (Ejercicios 7-1 a 7-3)
# 7-1 Coche de alquiles: Input básico
coche = input("¿Que tipo de coche te gustaria alquilar? ")
print(f"Dejame ver si puedo encontrar un {coche}.")

# 7-3 Multiplos de diez: El operador % devuelve 0 si la division es exacta.
numero = input("Dime un número por favor: ")
numero = int(numero) # Convertimos el texto a entero

if numero % 10:
    print(f"El número {numero} es múltiplo de 10.")
else:
    print(f"El número {numero} no es múltiplo de 10.")

# Bloque 2: Bucles while(Ejercicios 7-4 a 7-7)
# El objetivo es mantener el pragrama corriendo hasta que el usuario decida salir.
# 7-4 Ingredientes de la pizza: el bucle se repetira hasta que el usuario escriba 'quit'
prompt = "\n Introduce un ingrediente para tu pizza:"
prompt += "\n(Escribe 'quit para terminar): "

while True:
    ingredientes = input(prompt)

    if ingredientes == 'quit':
        break # Rompe el bucle inmediatamente
    else: 
        print(f"¡Añadire {ingredientes} a la pizza!")

# 7-5 Entradas de cine: combina bucle while con lógica condicional de precios segun edad.
prompt = "Dime tu edad (o escribe 'quit' para salir): "

while True:
    edad_input = input(prompt)

    if edad_input == 'quit':
        break

    # Convertimos e entero solo si no escribe 'quit'
    edad = int(edad_input)

    if edad < 3:
        print("La entrada es gratis.")
    elif edad <12:
        print("La entrada cuesta $10.")
    else:
        print("La entrada cuesta $15.")

# 7-8 Deli (Mover ítems de una lista a otra): 
sandwich_orders = ['atun', 'pollo', 'jamón', 'vegetal']
finished_sandwiches = []

# Mientras la lista de pedidos no esté vacía:
while sandwich_orders:
    # .pop() saca el último elemento y lo guarda en una variable
    sandwich_actual = sandwich_orders.pop()

    print(f"Preparando tu sándwich de {sandwich_actual}...")

    # Lo metemos en la lista de terminados
    finished_sandwiches.append(sandwich_actual)

print("\n--- Sándwiches Listos ---")
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-9 No pastrami(Eliminar todas las instacias): El metodo .remove() solo borra la primeri aparicion
sandwich_orders = ['pastrami', 'atún', 'pastrami', 'pollo', 'pastrami']

print("Lo sentimos, se nos ha acabado el pastrami.")

# Mientras 'pastrami' siga existiendo dentro de la lista:
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
# Salida: ['atún', 'pollo']