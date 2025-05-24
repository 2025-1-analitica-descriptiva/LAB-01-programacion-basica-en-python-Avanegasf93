"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    # Ruta del archivo de entrada
    ruta_archivo = r"D:\Github\Descriptiva\LAB-01-programacion-basica-en-python-Avanegasf93\files\input\data.csv"

    # Diccionario para acumular la suma por cada letra de la columna 1
    suma_por_letra = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")

            letra_col1 = partes[0]               # Columna 1
            pares_col5 = partes[4].split(",")    # Columna 5

            suma_valores = sum(int(valor.split(":")[1]) for valor in pares_col5)

            # Acumulamos por letra
            if letra_col1 in suma_por_letra:
                suma_por_letra[letra_col1] += suma_valores
            else:
                suma_por_letra[letra_col1] = suma_valores

    # Ordenamos alfabéticamente por la letra (clave)
    return dict(sorted(suma_por_letra.items()))

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_12()
    print("Resultado:", resultado)

