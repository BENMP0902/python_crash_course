# =========================================================================
# Ejercicio de Manipulación de Listas en Python (Capítulos 2, 3 y 4)
# =========================================================================

# Inicialización de la lista de invitados
nombres = ['Benjamin', 'Joel', 'Bruno']
mensaje_invitacion = "Te invito a cenar, no faltes"
mensaje_cancelacion = "Lo siento, la mesa se ha reducido. Tendrás que venir en otra ocasión."

# Variables auxiliares para cálculos
longitud = len(nombres)
indice_central = longitud // 2  # 3 // 2 = 1. Este índice es la posición de 'Joel' al inicio.

print("=" * 60)
print("INICIO DEL PROCESO DE GESTIÓN DE INVITACIONES")
print("=" * 60)

# -------------------------------------------------------------------------
# PARTE 1: Invitación Inicial (Uso de f-strings y .join())
# -------------------------------------------------------------------------

# 1. Muestra la lista inicial de invitados separada por comas y espacios.
# El método .join() une todos los elementos de la lista con el separador ', '
print(f"Buenos días, invitados iniciales: {', '.join(nombres)}\n")
print("-" * 60)

print("--- MENSAJES DE INVITACIÓN INICIAL ---")
# Imprime el mensaje individual para cada invitado usando un bucle 'for'
# El bucle recorre la lista 'nombres', asignando cada elemento a la variable 'nombre'.
for nombre in nombres:
    # f-string: permite insertar la variable 'nombre' directamente en la cadena.
    print(f"Estimado {nombre}, ¡ven a cenar!")
print("-" * 60)


# -------------------------------------------------------------------------
# PARTE 2: Manejo de Invitados No Disponibles (Reemplazo por índice)
# -------------------------------------------------------------------------

# Bruno no puede asistir. 'Bruno' está en el índice 2 (el último).
# Usamos el índice -1 (el último) para mayor robustez, aunque 2 también funciona.
invitado_ausente = nombres[-1]
print(f"AVISO: {invitado_ausente} no está disponible para la cena.")

# Se reemplaza al invitado ausente ('Bruno') por 'Abi'.
# Se usa la asignación directa por índice.
nombres[-1] = "Abi"  # Asigna 'Abi' al índice del último elemento.
print(f"Lista de invitados reemplazada: {nombres}")
print("-" * 60)

print("--- REENVÍO DE INVITACIONES (Lista de 3) ---")
# Se reenvía la invitación a la lista modificada
for nombre in nombres:
    print(f"¡{nombre}, te confirmo la cena!")
print("-" * 60)


# -------------------------------------------------------------------------
# PARTE 3 y 4: Encontrar una Mesa Grande (Inserción y Adición)
# -------------------------------------------------------------------------

print("NOTICIA: He encontrado una mesa más grande. ¡Más invitados se unen!")

# 1. Insertar nombre al inicio (Maru)
# .insert(indice, valor): inserta el valor ANTES del índice especificado.
nombres.insert(0, "Maru") # Inserta 'Maru' en el índice 0.
print(f"Paso 1 (Insertar 'Maru' al inicio): {nombres}")

# 2. Recalcular el índice central para la inserción al medio.
# Longitud actual: 4. El índice central ahora es 4 // 2 = 2.
indice_central_nueva = len(nombres) // 2

# 3. Insertar nombre al medio de la lista (Omar)
n_i = "Omar"
# Inserta 'Omar' en el índice 2, justo en el medio.
nombres.insert(indice_central_nueva, n_i)
print(f"Paso 2 (Insertar 'Omar' en el centro, índice {indice_central_nueva}): {nombres}")

# 4. Insertar mediante .append() al final (Jose)
# .append(valor): siempre añade el elemento al final de la lista.
nombres.append("Jose")
print(f"Paso 3 (Añadir 'Jose' al final con .append()): {nombres}")

print("-" * 60)

print(f"--- Invitaciones finales ({len(nombres)} invitados) ---")
# Envío de mensajes a la lista final de 6 invitados
for invitado in nombres:
    print(f"¡{invitado}! {mensaje_invitacion}.")
print("-" * 60)


# -------------------------------------------------------------------------
# PARTE 5: Mesa Reducida a 2 Personas (Eliminación con .pop())
# -------------------------------------------------------------------------

print("PROBLEMA: La reserva se ha reducido a solo 2 lugares. ¡Debo cancelar a 4!")

invitados_eliminados = []

# La lista actual tiene 6 personas. Debemos eliminar 4 para dejar 2.

# 1. Eliminar el último (por defecto si no se da índice)
# pop() elimina 'Jose' (el último) y lo devuelve.
eliminado_1 = nombres.pop()
invitados_eliminados.append(eliminado_1)
print(f"pop(): Eliminado del final: {eliminado_1}. Lista actual: {nombres}")

# 2. Eliminar el primero (índice 0)
# pop(0) elimina 'Maru' y lo devuelve. Los índices se reajustan.
eliminado_2 = nombres.pop(0)
invitados_eliminados.append(eliminado_2)
print(f"pop(0): Eliminado del inicio: {eliminado_2}. Lista actual: {nombres}")
# Lista actual: ['Benjamin', 'Omar', 'Joel', 'Abi']

# 3. Eliminar el segundo elemento restante (índice 1)
# pop(1) elimina 'Omar'. Los índices se reajustan.
eliminado_3 = nombres.pop(1)
invitados_eliminados.append(eliminado_3)
print(f"pop(1): Eliminado del centro: {eliminado_3}. Lista actual: {nombres}")
# Lista actual: ['Benjamin', 'Joel', 'Abi']

# 4. Eliminar otro del centro (índice 1)
# pop(1) elimina 'Joel'.
eliminado_4 = nombres.pop(1)
invitados_eliminados.append(eliminado_4)
print(f"pop(1): Eliminado del centro: {eliminado_4}. Lista actual: {nombres}")
# Lista final de la Parte 5: ['Benjamin', 'Abi']

print("-" * 60)

print("--- Mensajes de cancelación a los 4 eliminados ---")
# Enviamos el mensaje de cancelación a todos los guardados en la lista auxiliar
for persona_eliminada in invitados_eliminados:
    print(f"Estimado/a {persona_eliminada}, {mensaje_cancelacion}")

print("-" * 60)

print(f"--- Invitaciones Finales (Mesa reducida de {len(nombres)} personas) ---")
# Enviamos la invitación a los dos únicos restantes
for invitado_final in nombres:
    print(f"¡{invitado_final}! ¡Tienes un lugar asegurado para la cena!")
print("-" * 60)


# -------------------------------------------------------------------------
# PARTE 6: Dejar lista vacía (Uso de del)
# -------------------------------------------------------------------------

print("ACCIÓN: Es hora de terminar el script y vaciar la lista.")

# La lista 'nombres' actual es: ['Benjamin', 'Abi']

# 1. Eliminar el primer elemento
# 'del' elimina el elemento en el índice 0 ('Benjamin').
# Los índices se reajustan (el elemento 1 pasa a ser el 0).
del nombres[0]
print(f"del nombres[0]: Eliminado 'Benjamin'. Lista actual: {nombres}")

# 2. Eliminar el elemento restante
# 'del' elimina el único elemento restante ('Abi') que ahora está en el índice 0.
del nombres[0]
print(f"del nombres[0]: Eliminado 'Abi'. Lista actual: {nombres}")

# 3. Verificación de lista vacía
print("-" * 60)
print("--- VERIFICACIÓN DE LISTA VACÍA ---")

# Comprueba la longitud de la lista. Una lista vacía tiene longitud 0.
longitud_final = len(nombres)
print(f"Longitud final de la lista 'nombres': {longitud_final}")

if longitud_final == 0:
    print("VERIFICACIÓN EXITOSA: La lista está completamente vacía.")
else:
    print("ERROR: La lista no está vacía. Su longitud es {longitud_final}.")

print("=" * 60)
print("FIN DEL PROCESO")