# Modulos_y_Paquetes_en_Python

Se realizo en proyecto separando el codigo en modulos y paquetes, para una mejor organizacion y reutilizacion del codigo.

## Módulos

Un módulo es un archivo que contiene código Python, incluyendo funciones, clases y variables.

## Paquetes

Un paquete es una colección de módulos organizados en una estructura de directorios.

# Dia 1: 27/01/2026

## Modulos y Organizacion de codigo

En el dia 1 se realizaron operaciones basicas como suma, resta, multiplicacion y division, separando el codigo en modulos y paquetes, para una mejor organizacion y reutilizacion del codigo, luego fue importado a un archivo main.py para verificar su funcionamiento.

# Dia 2: 28/01/2026

## Importacion avanzada y Seguridad

En el dia 2 se realizo la importacion de un modulo externo llamado math, que contiene funciones matematicas como raiz cuadrada y potencia, ademas de la importacion selectiva de funciones y la importacion con alias.

- `import modulo`: Importa el módulo completo.
- `from modulo import funcion`: Importa una función específica del módulo.
- `from modulo import *`: Importa todas las funciones del módulo.
- `from modulo import funcion as alias`: Importa una función con un alias.

Tambien se mostro el contenido de la variable sys.path, en donde se nos plantea la siguiente pregunta: ¿Por que Python busca primero en el directorio actual?

La respuesta es que Python busca primero en el directorio actual para evitar conflictos con módulos del sistema que tengan el mismo nombre que los módulos locales. Si Python buscara primero en los directorios del sistema, podría sobrescribir módulos del sistema con módulos locales que tengan el mismo nombre.
