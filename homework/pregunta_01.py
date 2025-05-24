"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
def pregunta_01():
    """
    Retorne la suma de la segunda columna del archivo 'data.csv'.
    Rta/ 214
    """
    # Ruta absoluta al archivo de entrada
    ruta_archivo = "files/input/data.csv"

    # Variable para acumular la suma
    suma_columna_2 = 0

    # Abrimos el archivo en modo lectura con codificación UTF-8
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        # Iteramos por cada línea del archivo
        for line in file:
            # Eliminamos saltos de línea y separamos por tabulador
            partes = line.strip().split("\t")

            # Verificamos que haya al menos dos columnas
            if len(partes) > 1:
                # Sumamos el valor entero de la segunda columna
                suma_columna_2 += int(partes[1])

    # Retornamos el resultado final
    return suma_columna_2

# Código para ejecutar la función si este script se corre directamente
if __name__ == "__main__":
    resultado = pregunta_01()
    print("Resultado:", resultado)


