"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.
    
    Rta/ [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    # Ruta absoluta al archivo de entrada
    ruta_archivo = "files/input/data.csv"

    # Diccionario para llevar el conteo de letras
    conteo = {}

    # Abrimos el archivo en modo lectura con codificación UTF-8
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        # Iteramos por cada línea del archivo
        for linea in file:
            # Eliminamos saltos de línea y separamos por tabulador
            partes = linea.strip().split("\t")

            # Tomamos la letra de la primera columna
            letra = partes[0]

            # Si ya está en el diccionario, incrementamos el contador
            if letra in conteo:
                conteo[letra] += 1
            # Si no está, la inicializamos con 1
            else:
                conteo[letra] = 1

    # Convertimos el diccionario en lista de tuplas y la ordenamos alfabéticamente por letra
    resultado = sorted(conteo.items())

    # Retornamos la lista ordenada
    return resultado

# Código para ejecutar la función si este script se corre directamente
if __name__ == "__main__":
    resultado = pregunta_02()
    print("Resultado:", resultado)
