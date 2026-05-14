import sqlite3
import csv
import os

def insertar_autores_desde_csv(nombre_archivo_csv, nombre_db):
    # Obtener la ruta absoluta de la carpeta donde está este script de python
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Construir la ruta completa: directorio_del_script / data / info.csv
    ruta_completa_csv = os.path.join(directorio_actual, 'data', nombre_archivo_csv)
    
    # También podemos asegurar la ruta de la base de datos si está en la raíz
    ruta_completa_db = os.path.join(directorio_actual, nombre_db)

    try:
        conexion = sqlite3.connect(ruta_completa_db)
        cursor = conexion.cursor()

        if not os.path.exists(ruta_completa_csv):
            print(f"Error: El archivo no existe en la ruta: {ruta_completa_csv}")
            return

        with open(ruta_completa_csv, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv, None) # Saltar cabecera

            sql = "INSERT INTO Autor (nombre, apellido, cedula, edad) VALUES (?, ?, ?, ?)"
            cursor.executemany(sql, lector_csv)

        conexion.commit()
        print(f"¡Éxito! Datos insertados desde: {ruta_completa_csv}")

    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        if conexion:
            conexion.close()

# Uso del script
# Solo pasas el nombre del archivo, la lógica interna busca la carpeta 'data'
insertar_autores_desde_csv('info.csv', 'base_ejemplo.db')