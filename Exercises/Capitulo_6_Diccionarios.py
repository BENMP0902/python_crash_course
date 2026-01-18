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
# --------------------------------------------------------------------------

# Bloque 3: Anidamiento (Nesting)(Ejercicio 6-7 a 6-12)
# Significa guardar una lista dentro de un diccionario, o un diccionario dentro de una lista.

# 6-9 lugares favoritos(Lista dentro de un diccionario)
favorite_places = {
    'ana': ['paris', 'roma'],
    'juan': ['machu pichu'],
    'luis': ['tokyo', 'kyoto', 'osaka']
}

# El primer buclr accede a la persona y a su LISTA de lugares
#items accede tanto al indice como al valor 
for name, places in favorite_places.items():
    print(f"\nA {name.title()} le gusta visitar: ")

    # El segundo bucle recorre la LISTA especifica de esa persona
    for place in places:
        print(f"\t- {place.title()}")

# 6-11 Ciudades (Diccionario dentro de un diccionario): Es como un archuvo JSON.Tiene
# claves principales(nombres de ciudades) y el valor de cada una es otro diccionario con detalles.
cities = {
    'santiago': {
        'country': 'chile',
        'population': '6 millones', 
        'fact': 'Esta cerca de los Andes.'
    },
    'tokyo': {
        'country': 'japon',
        'population': '14 millones',
        'fact': 'Es la ciudad mas poblada'
    },
    'paris': {
        'country': 'francia',
        'population': '2 millones',
        'fact': 'Es conocido como la ciudad de la luz.'
    }
}

for city, city_info in cities.items():
    print(f"\nCiudad: {city.title()}")
    # Accedemos a los datos dentro del diccionario interno
    country = city_info['country']
    pop = city_info['population']
    fact = city_info['fact']

    print(f"\t-País: {country.title()}")
    print(f"\t-Poblacion: {pop}")
    print(f"\t-Dato curioso: {fact}")
