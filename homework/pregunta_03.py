"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma), ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    # Ruta al archivo CSV de entrada
    ruta_archivo = r"D:\Github\Descriptiva\LAB-01-programacion-basica-en-python-Avanegasf93\files\input\data.csv"

    # Diccionario para almacenar la suma de valores por cada letra
    sumas = {}

    # Abrimos el archivo en modo lectura con codificación UTF-8
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        # Iteramos sobre cada línea del archivo
        for linea in file:
            # Limpiamos la línea y separamos por tabulador
            partes = linea.strip().split("\t")

            # Obtenemos la letra de la primera columna y el número de la segunda
            letra = partes[0]
            valor = int(partes[1])

            # Acumulamos la suma por letra
            if letra in sumas:
                sumas[letra] += valor
            else:
                sumas[letra] = valor

    # Convertimos el diccionario en una lista de tuplas ordenada alfabéticamente
    resultado = sorted(sumas.items())

    # Retornamos la lista resultante
    return resultado

# Código para probar la función si se ejecuta directamente
if __name__ == "__main__":
    resultado = pregunta_03()
    print("Resultado:", resultado)
