# Bloque 1: Pruebas condicionales (Ejercicios 5-1 y 5-2)
# Objetivo comprender los operadores de comparacion (==,!=, <,>,etc.) y lógica (and, or).

#5-1. Pruebas condicionales: Escribir series de pruebas que predigan True o False.
car = 'subaru'

print("¿El carro es == 'subaru'? Predigo True")
print(car == 'subaru') # True

print("\n¿Es car == 'audi'? Predigo False.")
print(car == 'audi')   # False

# Ojo: Python distingue mayúsculas de minúsculas
print("\n¿Es car == 'Subaru'? Predigo False.")
print(car == 'Subaru') # False (porque la 'S' es mayúscula)
print('-'*30)

# Bloque 2: La Cadena if-elif-else (Ejercicios 5-3 a 5-7)
#Estos son los famosos ejercicios de "Colores de Aliens". 
#Te enseñan a estructurar decisiones simples, alternativas y múltiples.

# 5-3, 5-4 y 5-5. Colores de alienígenas (La evolución): Aquí combinamos la lógica. 
# Supongamos que disparas a un alienígena en un juego.

# Version completa (5-5) con if-elif-else:
alien_color = 'rojo'

if alien_color == 'verde':
    print("¡Ganaste 5 puntos!")
elif alien_color == 'amarillo':
    print("¡Ganaste 10 puntos!")
else:
    # Si no es verde ni amarillo se asume rojo
    print("¡Ganaste 15 puntos!")
print('-'*30)

# 5-6. Etapas de la vida: Este ejercicio es genial para entender los rangos numéricos.
age = 25

if age < 2:
    print("Es un bebé.")
elif age < 4:
    print("Es un infante.")
elif age < 13:
    print("Es un niño.")
elif age < 20:
    print("Es un adolecente.")
elif age < 65:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")    
print('-'*30)

# Bloque 3: Listas + If (Ejercicios 5-8 a 5-11)
# Aquí es donde se pone interesante: usar bucles for combinados con if para procesar listas.

# 5-8. Hola Admin: Saludar de forma especial al administrador y genérica a los demás.
usuarios = ['admin', 'jairo', 'maria', 'dani', 'karla']

for usuario in usuarios:
    if usuario == 'admin':
        print("Hola admin ¿quieres ver un informe de estado?")
    else:
        # Usamos .title() para dar formalidad
        print(f"Hola {usuario.title()}, gracias por regresar.")
print('-'*30)

# 5-9. Sin usuarios (Listas vacías): Es vital verificar si una lista tiene datos antes de intentar procesarla.
usuarios_2 = []

if usuarios: # Pyhton evalua las listas vacias como False y con datos True
    for usuario in usuarios_2:
        print(f"Hola {usuario}")
    else:
        print("¡Necesitamos encontrar usuarios!") 
print('-'*30)

# 5-10. Comprobando nombres de usuario (Case sensitivity): Este es el ejercicio más difícil del capítulo.
#Simula un registro de web donde no puedes usar "Juan" si ya existe "juan".
current_users = ['Juan', 'Ana', 'Pedro', 'Sofia', 'Luis']
new_users = ['PEDRO','Maria', 'JUAN', 'Elena']

# Creamos una copia en minúsculas de la lista actual para comparar limpiamente
# Usamos List Comprehension del capitulo anterior
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # Comparamos con la lista en minusculas
    if new_user.lower() in current_users_lower:
        print(f"El nombre '{new_user}' ya esta en uso. Elige otro.")
    else:
        print(f"El nombre '{new_user}' esta disponble.")