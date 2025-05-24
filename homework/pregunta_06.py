"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del carácter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    # Ruta del archivo CSV
    ruta_archivo = "files/input/data.csv"

    # Diccionario para guardar los valores por clave
    valores_por_clave = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            # Separamos la línea por tabuladores
            partes = linea.strip().split("\t")

            # Extraemos la columna 5 (índice 4)
            columna_5 = partes[4]

            # Separamos los pares clave:valor por coma
            pares = columna_5.split(",")

            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)

                # Agregamos el valor al diccionario agrupado por clave
                if clave in valores_por_clave:
                    valores_por_clave[clave].append(valor)
                else:
                    valores_por_clave[clave] = [valor]

    # Generamos la lista de tuplas con clave, mínimo y máximo, ordenada alfabéticamente
    resultado = []
    for clave in sorted(valores_por_clave.keys()):
        min_val = min(valores_por_clave[clave])
        max_val = max(valores_por_clave[clave])
        resultado.append((clave, min_val, max_val))

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_06()
    print("Resultado:", resultado)

