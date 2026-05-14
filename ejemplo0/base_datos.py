"""
    Crear la base de datos de Python
"""
import sqlite3

# Definimos la ruta donde queremos que se guarde o se lea la base de datos.
# En este caso, se está guardando en el mismo directorio donde se encuentra este script.
import os
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_base_datos = os.path.join(directorio_actual, 'base_ejemplo.db')

conn = sqlite3.connect(ruta_base_datos)
