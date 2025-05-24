"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas que contenga, por cada fila, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    # Ruta del archivo
    ruta_archivo = "files/input/data.csv"

    resultado = []

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")

            letra = partes[0]                         # Columna 1
            elementos_col4 = partes[3].split(",")     # Columna 4 (lista separada por comas)
            elementos_col5 = partes[4].split(",")     # Columna 5 (lista separada por comas)

            resultado.append((letra, len(elementos_col4), len(elementos_col5)))

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_10()
    print("Resultado:", resultado)

