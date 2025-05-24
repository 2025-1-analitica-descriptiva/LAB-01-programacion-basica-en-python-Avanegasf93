"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 2 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    # Ruta al archivo CSV
    ruta_archivo = "files/input/data.csv"

    # Diccionario para mapear valores de columna 2 a letras de columna 1
    asociaciones = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            # Separar cada línea por tabuladores
            partes = linea.strip().split("\t")

            letra = partes[0]            # Columna 1: letra
            valor = int(partes[1])       # Columna 2: valor numérico

            # Asociamos valor -> lista de letras
            if valor in asociaciones:
                asociaciones[valor].append(letra)
            else:
                asociaciones[valor] = [letra]

    # Ordenamos por los valores de la columna 2
    resultado = sorted(asociaciones.items())

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_07()
    print("Resultado:", resultado)

