import sys
import os
import io
import pandas as pd

# 1. Obtener la ruta de la carpeta 'datos-de-entrada-ml-0040'
directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_datos = os.path.abspath(os.path.join(directorio_script, '..', 'datos-de-entrada-ml-0040'))

if ruta_datos not in sys.path:
    sys.path.insert(0, ruta_datos)

import dicc_0040 # type: ignore

print("Hugo Fabian Machine Learning pandas, NC 0040")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Hugo Fabian Machine Learning pandas, NC 0040"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# Detectar automáticamente los datos del módulo
if hasattr(dicc_0040, 'datos_productos'):
    datos = dicc_0040.datos_productos
elif hasattr(dicc_0040, 'datos_productos_0040'):
    datos = dicc_0040.datos_productos_0040
else:
    datos = [v for k, v in vars(dicc_0040).items() if not k.startswith("__") and isinstance(v, (dict, list))][0]

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(datos)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Precio)
registrar("3. Estadísticas Generales de la Columna 'Precio'", df['Precio'].describe())

# 4. Ordenar Ascendente por Precio
df_asc_precio = df.sort_values(by="Precio", ascending=True)
registrar("4. Ordenar Ascendente por Precio", df_asc_precio)

# 5. Ordenar Descendente por Cuerdas_teclas (Se cambió 'Stock' por 'Cuerdas_teclas')
df_desc_cuerdas = df.sort_values(by="Cuerdas_teclas", ascending=False)
registrar("5. Ordenar Descendente por Cuerdas_teclas", df_desc_cuerdas)

# 7. Guardar el archivo resultados-ml-0040.md dentro de resultados-0040
carpeta_resultados = os.path.abspath(os.path.join(directorio_script, '..', 'resultados-0040'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0040.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Hugo Fabian Machine Learning pandas, NC 0040")