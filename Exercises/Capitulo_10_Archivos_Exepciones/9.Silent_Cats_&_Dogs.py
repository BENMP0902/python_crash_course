from pathlib  import Path

filenames = ['cats.txt', 'dogs.txt',]

for filename in filenames:
    path = Path(filename)

    try: 
        contents = path.read_text(encoding='utf-8')

        print(f"\n-{filename}-")
        print(contents)
    
    except FileNotFoundError:
        pass #Falla silenciosamente - no hace nada
#-------------------------------------------------------------------------------
# Mejores prácticas actuales:
filename = ['cats.txt', 'dogs.txt', 'birds.txt']

print("=== VERSIÓN 1: Falla Silenciosa ===")
for filename in filenames:
    try:
        contents = Path(filename).read_text(encoding='utf-8')
        print(f"\n{filename}:")
        print(contents)
    except FileNotFoundError:
        pass  # No muestra nada si el archivo no existe

print("\n" + "="*50)
print("=== VERSIÓN 2: Con Información ===")
for filename in filenames:
    try:
        contents = Path(filename).read_text(encoding='utf-8')
        print(f"\n✓ {filename}:")
        print(contents)
    except FileNotFoundError:
        print(f"✗ {filename}: No encontrado (omitido)")

#--------------------------------------------------------------------------------------
# Verision con contador de archivos procesados
def read_files_silently(filenames):
       """
       Lee archivos silenciosamente, solo muestra los que existen.
       
       Returns:
           Número de archivos leídos exitosamente
       """
       successful_reads = 0
       
       for filename in filenames:
           try:
               contents = Path(filename).read_text(encoding='utf-8')
               print(f"\n=== {filename} ===")
               print(contents)
               successful_reads += 1
               
           except FileNotFoundError:
               pass  # Ignorar archivos no encontrados
       
       return successful_reads
   
# Uso
files = ['cats.txt', 'dogs.txt', 'birds.txt']
count = read_files_silently(files)

# Solo mostrar resumen al final
if count > 0:
    print(f"\n📊 Se leyeron {count} archivo(s) exitosamente.")
else:
    print("\n⚠ No se pudo leer ningún archivo.")

#-------------------------------------------------------------------------------------
# Version con loggin silencioso en segundo plano
from datetime import datetime

def silent_read_with_logging(filenames):
    """
    Lee archivos silenciosamente pero registra errores en un log.
    """
    log_entries = []
    
    for filename in filenames:
        path = Path(filename)
        
        try:
            contents = path.read_text(encoding='utf-8')
            print(f"\n{filename}:")
            print(contents)
            
        except FileNotFoundError:
            # Registrar error sin mostrarlo
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entries.append(f"[{timestamp}] Archivo no encontrado: {filename}")
    
    # Guardar log si hubo errores
    if log_entries:
        log_path = Path('silent_errors.log')
        log_content = '\n'.join(log_entries)
        
        if log_path.exists():
            current = log_path.read_text(encoding='utf-8')
            log_path.write_text(current + '\n' + log_content, encoding='utf-8')
        else:
            log_path.write_text(log_content, encoding='utf-8')

# Uso
files = ['cats.txt', 'dogs.txt', 'birds.txt']
silent_read_with_logging(files)