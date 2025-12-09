# 1. Asigna el valor del nombre de archivo a la variable
nombre_de_archivo = "python_notes.txt"

# 2. Usa el método .removesuffix() para eliminar la extensión ".txt"
# Se le pasa el sufijo (la parte que quieres eliminar) como argumento.
nombre_sin_extension = nombre_de_archivo.removesuffix(".txt")

# 3. Imprime el resultado
print("Nombre de archivo original:", nombre_de_archivo)
print("Nombre sin extensión:", nombre_sin_extension)