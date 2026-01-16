# Un Diccionario asocia una clave con un valor y se accede por nmbre en lugar de por índice.
# Bloque 1 Diccionarios simples(Ejercicis 6-1 a 6-3)

persona = {
    'first_name': 'Elon',
    'last_name': 'Musk',
    'age': 52,
    'city': 'Austin'
}

print(persona['first_name'])
print(persona['last_name'])
print(persona['age'])
print(persona['city'])

# Blque 2: Recorriendo un Diccionario(Ejercicios 6-4 a 6-6)
# A diferencia de las listas, en los diccionarios 
# puedes iterar de tres formas: -solo los valores.
#                               -solo las clabves.
#                               -ambos a la vez.

# 6-5 Rios: Un diccionario donde la clave es el rio y el valor es el pais
rios = {
    'nilo': 'egipto',
    'amazonas': 'brasil',
    'mississipi': 'estados unidos'
}
# 1. Imprimir una frase usando ambos (items)
# .items() nos devuelve la pareja (clave, valor)
for rio, pais in rios.items():
    print(f"El río {rio.title()} corre a través de {pais.title()}.")

print("\n--- Ríos ---")

# 2. Imprimir solo el nombre del río (keys)
for rio in rios.keys():
    print(rio.title())

print("\n--- Países ---")
# 3. Imprimir solo el país (values)
for pais in rios.values():
    print(pais.title())