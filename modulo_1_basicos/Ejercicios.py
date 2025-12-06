# ==========================================
# MODULO 1: Fundamentos de Python
# Archivo: main.py
# ==========================================

print("--- EJERCICIO 1: Variables y Tipos de Datos ---")
# Objetivo: Definir variables de diferentes tipos y mostrarlas.

nombre_usuario = "BENMP"        # String (Texto)
edad = 29                         # Integer (Entero)
altura = 1.60                     # Float (Decimal)
es_estudiante = True              # Boolean (Verdadero/Falso)

# Usamos f-strings (la f antes de las comillas) para insertar variables en texto
print(f"Perfil cargado: {nombre_usuario}")
print(f"Edad: {edad} años | Altura: {altura}m")
print(f"¿Estado activo?: {es_estudiante}")
print("-" * 30) # Separador visual


print("\n--- EJERCICIO 2: Operaciones Matemáticas ---")
# Objetivo: Calcular el área de un proyecto imaginario (Rectángulo).

base = 10
altura_rect = 5

area = base * altura_rect
perimetro = (base + altura_rect) * 2

print(f"Dimensiones: Base {base} x Altura {altura_rect}")
print(f"Área calculada: {area} m²")
print(f"Perímetro calculado: {perimetro} m")
print("-" * 30)


print("\n--- EJERCICIO 3: Interacción (Input) y Casting ---")
# Objetivo: Pedir datos al usuario y convertirlos para calcular su año de nacimiento.
# NOTA: input() siempre devuelve texto (string), por eso usamos int() para convertirlo.

edad_ingresada = input("Ingresa tu edad actual: ") # El programa se pausa aquí
anio_actual = 2025

# Conversión de tipo (Casting): De Texto -> Entero
edad_numero = int(edad_ingresada)

anio_nacimiento = anio_actual - edad_numero

print(f"Sistema detecta que naciste aproximadamente en: {anio_nacimiento}")
print("-" * 30)


print("\n--- EJERCICIO 4: Manipulación de Strings ---")
# Objetivo: Métodos básicos para limpiar texto.

codigo_sucio = "  python-crash-course  "

print(f"Texto original: '{codigo_sucio}'")
print(f"1. Strip (quitar espacios): '{codigo_sucio.strip()}'")
print(f"2. Upper (mayúsculas): '{codigo_sucio.upper().strip()}'")
print(f"3. Replace (reemplazar): '{codigo_sucio.replace('-', '_').strip()}'")

print("\n=== MÓDULO 1 COMPLETADO CON ÉXITO ===")