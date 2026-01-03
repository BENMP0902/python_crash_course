# Creamos lista principal
pizzas = ['pepperoni', 'hawaina', 'mexicana']

# Parte 1: Imprimir solo el nombre
for pizza in pizzas:
    print(pizza)

print("\n") # Salto de linea para separar

# Parte 2: Imprimir oracion
for pizza in pizzas:
    print(f"Me gusta mucho la pizza de {pizza}.")

# Parte 3: Fuera del bucle (sin identificacion)
print("\nRealmente amo las pizzas")

# Se realiza el mismo proceso con nombres de animales en el 4-2

# 4-5 Sumar un millon(Crear una lista del 1 al un millon y sumarla)
numeros = list(range(1, 1000001))
print(min(numeros)) # 1
print(max(numeros)) # 1000000
print(sum(numeros)) # 500000500000

# 4-6 Numeros impares: Usar el tercer argumento de range() para saltar numeros impares.
impares = list(range(1, 21, 2))
for numero in impares:
    print(impares)

# 4-7 Saltos de 3
tres = list(range(3, 31, 3))
for numero in tres:
    print(tres)

# 4-8, 4-9 Cubos de numeros, [expresion for variable in coleccion]
cubos = [value**3 for value in range(1,11)]
print(cubos)

# 4-10 Slices(Rodajas/Rebanadas)
cubos = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

print("Los tres primeros elementos son:")
print(cubos[:3])

print("Los tres elementos de en medios son:")
print(cubos[3:6])

print("Los tres ultimos elementos son:")
print(cubos[-3:])

# 4-11 
friend_pizzas = pizzas[:]

pizzas.append('chorizo')
friend_pizzas.append('surtida')

print(pizzas)
print(friend_pizzas)

# 4-13 Buffet (Tuplas): Las Tuplas se definen con paréntesis () en lugar de corchetes [] y no se pueden modificar.
comidas = ('arroz', 'pollo', ' ensalada', 'sopa', 'pastel')
for comida in comidas:
    print(comida)

# comidas[0] = 'hamburgesa' # Daria error, Python no permite alterar la tupla

print("\nEl menú ha cambiado:")
# Debemos redefinir la variable completa para cambiarla
comidas = ('arroz', 'pescado', 'ensalada', 'crema', 'pastel')
for comida in comidas:
    print(comida)



