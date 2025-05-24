"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    # Ruta del archivo CSV
    ruta_archivo = "files/input/data.csv"

    # Diccionario para agrupar letras únicas por valor
    asociaciones = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")

            letra = partes[0]            # Columna 1
            valor = int(partes[1])       # Columna 2

            # Usamos un conjunto para evitar duplicados
            if valor in asociaciones:
                asociaciones[valor].add(letra)
            else:
                asociaciones[valor] = set([letra])

    # Convertimos los conjuntos en listas ordenadas y armamos el resultado
    resultado = []
    for valor in sorted(asociaciones.keys()):
        letras_ordenadas = sorted(asociaciones[valor])
        resultado.append((valor, letras_ordenadas))

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_08()
    print("Resultado:", resultado)

