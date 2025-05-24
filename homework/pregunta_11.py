"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    # Ruta del archivo de entrada
    ruta_archivo = "files/input/data.csv"

    # Diccionario para acumular la suma de valores
    suma_por_letra = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")

            valor_col2 = int(partes[1])              # Columna 2 (valor numérico)
            letras_col4 = partes[3].split(",")       # Columna 4 (letras separadas por comas)

            # Sumamos el valor de col2 a cada letra en col4
            for letra in letras_col4:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_col2
                else:
                    suma_por_letra[letra] = valor_col2

    # Retornamos el diccionario ordenado alfabéticamente por clave
    resultado = dict(sorted(suma_por_letra.items()))

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_11()
    print("Resultado:", resultado)
