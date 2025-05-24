"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    # Ruta al archivo
    ruta_archivo = r"D:\Github\Descriptiva\LAB-01-programacion-basica-en-python-Avanegasf93\files\input\data.csv"

    # Diccionario para contar apariciones por clave
    conteo_claves = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")
            columna_5 = partes[4]  # Columna 5 contiene los pares clave:valor

            pares = columna_5.split(",")

            for par in pares:
                clave, _ = par.split(":")  # Solo tomamos la clave

                # Incrementamos el contador por clave
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1

    return conteo_claves

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_09()
    print("Resultado:", resultado)

