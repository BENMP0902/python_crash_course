# 🐍 Python Crash Course: Complete Learning Journey

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Kali-557C94?style=for-the-badge&logo=linux&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)
![Book](https://img.shields.io/badge/Book-3rd%20Edition%202023-green?style=for-the-badge)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/benjam%C3%ADn-mart%C3%ADnez-p%C3%A9rez-17949434b/)
[![GitHub](https://img.shields.io/badge/GitHub-BENMP0902-181717?style=flat&logo=github)](https://github.com/BENMP0902)

---

## 📚 Acerca de este Repositorio

Este repositorio documenta mi recorrido completo trabajando con **Python Crash Course, 3rd Edition (2023)** de Eric Matthes. Cada capítulo incluye ejercicios resueltos, mejores prácticas modernas de Python, código limpio y comentado siguiendo los estándares PEP 8.

### 🎯 Objetivos del Proyecto

- ✅ Dominar Python desde fundamentos hasta nivel avanzado
- ✅ Aplicar mejores prácticas profesionales (PEP 8, Clean Code, Type Hints)
- ✅ Usar herramientas modernas (`pathlib`, comprehensions, f-strings)
- 🎯 Construir proyectos del mundo real
- 🚀 Preparación para desarrollo profesional y MLOps

---

## 🚀 Cómo usar este Repositorio

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/BENMP0902/python_crash_course.git
cd python_crash_course
```

### 2️⃣ Crear entorno virtual (Recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Ejecutar ejercicios
```bash
# Navegar a un capítulo específico
cd Capitulo_10_Archivos_Excepciones

# Ejecutar un ejercicio
python3 1.Learning_python.py
```

---

## 📖 Índice de Contenidos

### **PARTE I: FUNDAMENTOS** 🏗️

#### ✅ Capítulo 2: Variables y Tipos de Datos Simples
- Variables y convenciones de nombres
- Strings y métodos de strings
- Números (integers, floats)
- Comentarios

#### ✅ Capítulo 3: Listas (Introducción)
- Crear y acceder listas
- Modificar, añadir y eliminar elementos
- Organizar listas (sort, reverse)
- Evitar errores de índice

#### ✅ Capítulo 4: Trabajar con Listas
- Loops `for`
- Funciones numéricas (range, min, max, sum)
- List comprehensions
- Slicing y copying listas
- Tuplas

#### ✅ Capítulo 5: Sentencias If
- Pruebas condicionales
- if, elif, else
- Listas y condicionales
- Verificar valores y listas vacías

#### ✅ Capítulo 6: Diccionarios
- Crear y usar diccionarios
- Modificar diccionarios
- Loops con diccionarios
- Diccionarios anidados
- Estructuras de datos complejas

#### ✅ Capítulo 7: Input y Loops While
- Función `input()`
- Loops `while`
- Control de flujo (break, continue)
- Usar while con listas y diccionarios
- Flags y manejo de múltiples condiciones

#### ✅ Capítulo 8: Funciones
- Definir funciones
- Parámetros y argumentos (posicionales, keyword, default)
- Return values
- Listas y diccionarios con funciones
- Módulos e importaciones
- Docstrings y documentación

#### ✅ Capítulo 9: Clases
- Crear y usar clases
- Atributos y métodos
- Herencia
- Importar clases
- La librería estándar de Python
- Estilizar clases (PEP 8)

**📂 Ejercicios completados:**
- ✅ Restaurant, User, Battery (Herencia)
- ✅ Admin, Privileges (Herencia múltiple)
- ✅ Ice Cream Stand, Users (Importaciones)

---

### **PARTE II: ARCHIVOS Y EXCEPCIONES** 📁

#### ✅ Capítulo 10: Archivos y Excepciones

**🔹 Lectura de Archivos**
- Uso de `pathlib.Path` (método moderno Python 3.4+)
- `read_text()` vs `open()` (legacy)
- Lectura línea por línea con `splitlines()`
- Rutas relativas vs absolutas

**🔹 Escritura en Archivos**
- `write_text()` para crear/sobrescribir archivos
- Encoding UTF-8 explícito
- Almacenamiento de múltiples líneas

**🔹 Excepciones**
- Bloques `try-except-else-finally`
- `FileNotFoundError`
- `ValueError` y `ZeroDivisionError`
- Fallar silenciosamente con `pass`
- Manejo robusto de errores

**🔹 Análisis de Texto**
- Método `count()` para búsqueda simple
- Regex con `re.findall()` para búsqueda precisa
- Procesamiento de archivos grandes
- Análisis de frecuencia de palabras

**📂 Ejercicios completados:**
```
✅ 10-1: Learning Python          (Lectura básica)
✅ 10-2: Learning C                (Método replace)
✅ 10-3: Simpler Code             (Eliminación de variables temporales)
✅ 10-4: Guest                     (Escritura simple)
✅ 10-5: Guest Book                (Escritura múltiple con loops)
✅ 10-6: Addition                  (Manejo de ValueError)
✅ 10-7: Addition Calculator       (Loop con excepciones)
✅ 10-8: Cats and Dogs            (FileNotFoundError)
✅ 10-9: Silent Cats and Dogs     (Fallas silenciosas)
✅ 10-10: Common Words             (Análisis de texto Project Gutenberg)
```

**🎯 Mejores prácticas aplicadas:**
- ✅ `pathlib.Path` sobre `open()`
- ✅ Especificación explícita de encoding UTF-8
- ✅ Uso de `splitlines()` en lugar de `split('\n')`
- ✅ Method chaining para código más limpio
- ✅ Manejo robusto de errores con try-except
- ✅ Type hints y docstrings
- ✅ Programación orientada a objetos para análisis complejos

---

### **PARTE III: PROYECTOS** (Próximamente) 🚧

#### 📌 Proyecto 1: Alien Invasion (Pygame)
- [ ] Nave espacial y controles
- [ ] Aliens y colisiones
- [ ] Puntuación y niveles

#### 📌 Proyecto 2: Data Visualization
- [ ] Matplotlib
- [ ] Plotly
- [ ] API requests

#### 📌 Proyecto 3: Web Applications
- [ ] Django
- [ ] Deployment

---

## 🛠️ Tecnologías y Herramientas

| Categoría | Herramientas |
|-----------|-------------|
| **Lenguaje** | Python 3.11+ |
| **OS** | Kali Linux (WSL2) |
| **IDE** | VS Code |
| **Control de Versiones** | Git & GitHub |
| **Librerías Principales** | `pathlib`, `re`, `json`, `datetime` |
| **Estándares** | PEP 8, Type Hints, Docstrings |

---

## 📊 Progreso General

```
PARTE I: FUNDAMENTOS
██████████████████████████████ 100% (Capítulos 2-9)

PARTE II: ARCHIVOS Y EXCEPCIONES  
███████████████░░░░░░░░░░░░░░  50% (Capítulo 10 en progreso)

PARTE III: PROYECTOS
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% (Próximamente)
```

**📈 Estadísticas:**
- ✅ **Capítulos completados:** 9/20
- ✅ **Ejercicios resueltos:** 80+
- 🔄 **Capítulo actual:** 10 (Archivos y Excepciones)
- 📝 **Líneas de código:** 3000+

---

## 🎓 Conceptos Clave Dominados

### Fundamentos
- ✅ Variables, tipos de datos, operadores
- ✅ Estructuras de control (if, for, while)
- ✅ Funciones y módulos
- ✅ Listas, tuplas, diccionarios, sets
- ✅ List/Dict comprehensions

### Intermedio
- ✅ Programación Orientada a Objetos
- ✅ Herencia y polimorfismo
- ✅ Manejo de archivos (`pathlib`)
- ✅ Excepciones y debugging
- ✅ Expresiones regulares básicas

### Mejores Prácticas
- ✅ PEP 8 Style Guide
- ✅ Type hints y docstrings
- ✅ Clean code principles
- ✅ DRY (Don't Repeat Yourself)
- ✅ Error handling patterns

---

## 📁 Estructura del Proyecto

```
python_crash_course/
│
├── Capitulo_2_Variables/
│   └── ejercicios/
│
├── Capitulo_3_Listas/
│   └── ejercicios/
│
├── Capitulo_4_Trabajar_Listas/
│   └── ejercicios/
│
├── Capitulo_5_Sentencias_If/
│   └── ejercicios/
│
├── Capitulo_6_Diccionarios/
│   └── ejercicios/
│
├── Capitulo_7_Input_While/
│   └── ejercicios/
│
├── Capitulo_8_Funciones/
│   └── ejercicios/
│
├── Capitulo_9_Clases/
│   ├── 1.Restaurant.py
│   ├── 2.Usuario.py
│   ├── 3.Battery.py
│   └── ejercicios/
│
├── Capitulo_10_Archivos_Excepciones/
│   ├── 1.Learning_python.py
│   ├── 2.Learning_C.py
│   ├── 3.Simpler_Code.py
│   ├── 4.Guest.py
│   ├── 5.Guest_Book.py
│   ├── 6.Addition.py
│   ├── 7.Addition_Calculator.py
│   ├── 8.Cats_&_Dogs.py
│   ├── 9.Silent_Cats_&_Dogs.py
│   ├── 10.Common_Words.py
│   ├── gutenberg/
│   │   ├── alice_adventures.txt
│   │   ├── moby_dick.txt
│   │   └── little_women.txt
│   ├── cats.txt
│   ├── dogs.txt
│   ├── guest.txt
│   ├── guests_book.txt
│   ├── learning_python.txt
│   └── pi_digits.txt
│
├── modulo_1_basicos/
├── modulo_2_control_flujo/
├── modulo_3_estructura_datos/
├── .gitignore
└── README.md
```

---

## 🎯 Próximos Pasos

### Capítulo 10 (En Progreso)
- [ ] 10-11: Favorite Number (JSON dumps)
- [ ] 10-12: Favorite Number Remembered (JSON loads)
- [ ] 10-13: User Dictionary (JSON con diccionarios)
- [ ] 10-14: Verify User (Verificación de usuario)

### Capítulo 11: Testing
- [ ] Unit tests con `pytest`
- [ ] Testing de funciones
- [ ] Testing de clases
- [ ] Fixtures y parametrización

### Proyectos
- [ ] Alien Invasion Game
- [ ] Data Visualization Projects
- [ ] Web Application con Django

---

## 📝 Notas de Aprendizaje

### Lecciones Importantes del Capítulo 10

**1. `pathlib` es el estándar moderno**
```python
# ✅ Moderno (Python 3.4+)
from pathlib import Path
contents = Path('file.txt').read_text(encoding='utf-8')

# ❌ Legacy
with open('file.txt', encoding='utf-8') as f:
    contents = f.read()
```

**2. Siempre especificar encoding**
```python
# ✅ Explícito y seguro
Path('file.txt').read_text(encoding='utf-8')

# ❌ Puede fallar en diferentes sistemas
Path('file.txt').read_text()
```

**3. Method chaining para código limpio**
```python
# ✅ Conciso y claro
for line in Path('file.txt').read_text().splitlines():
    print(line)
```

**4. Manejo robusto de excepciones**
```python
try:
    data = Path('file.txt').read_text(encoding='utf-8')
except FileNotFoundError:
    print("Archivo no encontrado")
except UnicodeDecodeError:
    print("Error de codificación")
```

---

## 🤝 Contribuciones

Este es un repositorio de aprendizaje personal, pero sugerencias y feedback son bienvenidos. Si encuentras errores o tienes mejoras que proponer, no dudes en abrir un issue.

---

## 📞 Contacto

- **LinkedIn:** [Benjamín Martínez Pérez](https://www.linkedin.com/in/benjam%C3%ADn-mart%C3%ADnez-p%C3%A9rez-17949434b/)
- **GitHub:** [@BENMP0902](https://github.com/BENMP0902)
- **Email:** Disponible en mi perfil de GitHub

---

## 📚 Recursos Adicionales

- [Python Crash Course - Sitio Oficial](https://nostarch.com/python-crash-course-3rd-edition)
- [Python Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Project Gutenberg](https://www.gutenberg.org/) (Para ejercicio 10-10)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. El código es libre de usar para propósitos educativos.

---

## ⭐ Agradecimientos

- **Eric Matthes** por escribir un excelente libro
- **No Starch Press** por la publicación
- La comunidad de Python por los recursos infinitos

---

<div align="center">

**🐍 Happy Coding! 🐍**

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white)

*"El código limpio siempre parece haber sido escrito por alguien a quien le importa."* - Robert C. Martin

</div>
