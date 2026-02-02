# 10-10: Analísis y manejo de archivos de Project Gutenberg
# Usaremos el método 'count()' para averiguar cuantas veces aparece una palabra o frase en un string.
from pathlib import Path

def count_word_in_file(filename, word):
    """Cuenta cúantas veces aparece una palabra en un archivo"""
    path = Path(filename)

    try:
        contents = path.read_text(encoding='utf-8')
        # Contar la palabra (case-insensitive)
        count = contents.lower().count(word.lower())
        return count

    except FileNotFoundError:
        print(f"x Archivo '{filename}' no encontrado.")
        return None
    
# Lista de archivos a analizar
filenames = ['alice_adventures.txt', 'frankenstein.txt', 'moby_dick']

print("-Análisis de Frecuencia de Palabras-")

for filename in filenames:
    # Contaremos 'the', que incluye 'then', 'there', etc.
    count_the = count_word_in_file(filename, 'the')

    # Contar 'the' más preciso:
    count_the_space = count_word_in_file(filename, 'the ')

    if count_the is not None and count_the_space is not None:
        print(f"📄 {filename}:")
        print(f"   'the' aparece aproximadamente {count_the} veces")
        print(f"   'the ' aparece aproximadamente {count_the_space} veces")
        print(f"   Diferencia: {count_the - count_the_space}\n")

#------------------------------------------------------------------------------------------------------
# Mejores practicas actuales:

# Version con conteo de palabras usando regex:
import re
   
def count_word_accurate(text, word):
    """
    Cuenta palabras completas usando expresiones regulares.
    
    Args:
        text: El texto donde buscar
        word: La palabra a contar
    
    Returns:
        Número de ocurrencias de la palabra completa
    """
    # \b indica límite de palabra (word boundary)
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

def analyze_text_file(filename, words_to_count):
    """
    Analiza un archivo de texto y cuenta palabras específicas.
    
    Args:
        filename: Nombre del archivo
        words_to_count: Lista de palabras a contar
    
    Returns:
        Diccionario con resultados del análisis
    """
    path = Path(filename)
    
    try:
        contents = path.read_text(encoding='utf-8')
        
        # Estadísticas básicas
        total_chars = len(contents)
        total_words = len(contents.split())
        total_lines = len(contents.splitlines())
        
        # Contar cada palabra
        word_counts = {}
        for word in words_to_count:
            # Método simple (incluye parciales)
            simple_count = contents.lower().count(word.lower())
            
            # Método preciso (solo palabras completas)
            accurate_count = count_word_accurate(contents, word)
            
            word_counts[word] = {
                'simple': simple_count,
                'accurate': accurate_count,
                'difference': simple_count - accurate_count
            }
        
        return {
            'filename': filename,
            'success': True,
            'stats': {
                'characters': total_chars,
                'words': total_words,
                'lines': total_lines
            },
            'word_counts': word_counts
        }
        
    except FileNotFoundError:
        return {
            'filename': filename,
            'success': False,
            'error': 'Archivo no encontrado'
        }
    except UnicodeDecodeError:
        return {
            'filename': filename,
            'success': False,
            'error': 'Error de codificación'
        }

# Analizar múltiples archivos
files_to_analyze = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
words_to_find = ['the', 'and', 'a', 'to', 'of']

print("=== ANÁLISIS DE TEXTOS DE PROJECT GUTENBERG ===\n")

for filename in files_to_analyze:
    result = analyze_text_file(filename, words_to_find)
    
    if result['success']:
        print(f"📚 {result['filename']}")
        print(f"   Caracteres: {result['stats']['characters']:,}")
        print(f"   Palabras: {result['stats']['words']:,}")
        print(f"   Líneas: {result['stats']['lines']:,}")
        print()
        
        for word, counts in result['word_counts'].items():
            print(f"   '{word}':")
            print(f"      Simple: {counts['simple']:,}")
            print(f"      Precisa: {counts['accurate']:,}")
            print(f"      Diferencia: {counts['difference']}")
        print("\n" + "="*60 + "\n")
    else:
        print(f"✗ {result['filename']}: {result['error']}\n")
#------------------------------------------------------------------------------------------------------
# Version con analisis comparativo entre libros:import re
import re
class TextAnalyzer:
    """Analizador de textos literarios."""
    
    def __init__(self, filename):
        self.filename = filename
        self.path = Path(filename)
        self.contents = None
        self.loaded = False
    
    def load(self):
        """Carga el contenido del archivo."""
        try:
            self.contents = self.path.read_text(encoding='utf-8')
            self.loaded = True
            return True
        except FileNotFoundError:
            print(f"✗ '{self.filename}' no encontrado.")
            return False
        except UnicodeDecodeError:
            print(f"✗ Error de codificación en '{self.filename}'.")
            return False
    
    def count_word(self, word, exact=True):
        """Cuenta ocurrencias de una palabra."""
        if not self.loaded or self.contents is None:
            return 0
        
        if exact:
            # Contar solo palabras completas
            pattern = r'\b' + re.escape(word) + r'\b'
            return len(re.findall(pattern, self.contents, re.IGNORECASE))
        else:
            # Contar cualquier ocurrencia
            return self.contents.lower().count(word.lower())
    
    def get_word_frequency(self, word):
        """Calcula la frecuencia de una palabra como porcentaje."""
        if not self.loaded or self.contents is None:
            return 0.0
        
        total_words = len(self.contents.split())
        word_count = self.count_word(word, exact=True)
        
        if total_words == 0:
            return 0.0
        
        return (word_count / total_words) * 100
    
    def get_stats(self):
        """Retorna estadísticas del texto."""
        if not self.loaded or self.contents is None:
            return None
        
        words = self.contents.split()
        lines = self.contents.splitlines()
        
        return {
            'characters': len(self.contents),
            'words': len(words),
            'lines': len(lines),
            'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0
        }

# Comparar múltiples libros
books = {
    'alice.txt': 'Alice in Wonderland',
    'moby_dick.txt': 'Moby Dick',
    'little_women.txt': 'Little Women'
}

print("=== ANÁLISIS COMPARATIVO DE LITERATURA ===\n")

analyzers = {}

# Cargar todos los libros
for filename, title in books.items():
    analyzer = TextAnalyzer(filename)
    if analyzer.load():
        analyzers[title] = analyzer

if not analyzers:
    print("⚠ No se pudo cargar ningún libro.")
else:
    # Palabras comunes en inglés
    common_words = ['the', 'and', 'to', 'a', 'of', 'in', 'is', 'that']
    
    # Analizar cada libro
    for title, analyzer in analyzers.items():
        print(f"📖 {title}")
        print("="*60)
        
        stats = analyzer.get_stats()
        print(f"Estadísticas:")
        print(f"  • Palabras: {stats['words']:,}")
        print(f"  • Líneas: {stats['lines']:,}")
        print(f"  • Promedio longitud palabra: {stats['avg_word_length']:.1f}")
        print()
        
        print(f"Frecuencia de palabras comunes:")
        for word in common_words:
            count = analyzer.count_word(word)
            freq = analyzer.get_word_frequency(word)
            print(f"  • '{word}': {count:,} veces ({freq:.2f}%)")
        
        print("\n" + "="*60 + "\n")
    
    # Comparación específica de 'the'
    print("📊 COMPARACIÓN: Uso de 'the' entre libros")
    print("="*60)
    
    for title, analyzer in analyzers.items():
        count_simple = analyzer.count_word('the', exact=False)
        count_exact = analyzer.count_word('the', exact=True)
        freq = analyzer.get_word_frequency('the')
        
        print(f"{title}:")
        print(f"  Conteo simple: {count_simple:,}")
        print(f"  Conteo exacto: {count_exact:,}")
        print(f"  Diferencia: {count_simple - count_exact:,}")
        print(f"  Frecuencia: {freq:.2f}%")
        print()
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------