# 1. Crea una variable 'nombre' con espacios en blanco (incluyendo \t y \n) al principio y al final.
# La tabulación (\t) crea un gran espacio horizontal.
# La nueva línea (\n) crea un salto de línea vertical.
nombre_sucio = "\n\t   Elon Musk   \t\n"

# --- Parte 1: Imprimir el nombre con el espacio en blanco ---
print("--- Nombre con espacio en blanco ---")
print(nombre_sucio)

# Imprimir una línea de separación para mayor claridad
print("------------------------------------")


# --- Parte 2: Imprimir el nombre usando cada función de eliminación ---

# a) lstrip() - Elimina espacios a la izquierda (left side)
nombre_lstrip = nombre_sucio.lstrip()
print("--- Usando lstrip() ---")
print(nombre_lstrip)


# b) rstrip() - Elimina espacios a la derecha (right side)
nombre_rstrip = nombre_sucio.rstrip()
print("--- Usando rstrip() ---")
print(nombre_rstrip)


# c) strip() - Elimina espacios a ambos lados (left Y right)
nombre_strip = nombre_sucio.strip()
print("--- Usando strip() (la más común) ---")
print(nombre_strip)
