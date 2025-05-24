"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    # Ruta al archivo CSV
    ruta_archivo = "files/input/data.csv"

    # Diccionario para almacenar los valores de la columna 2 por letra
    valores_por_letra = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            # Limpiamos y separamos por tabulador
            partes = linea.strip().split("\t")
            letra = partes[0]
            valor = int(partes[1])

            # Agrupamos los valores por letra
            if letra in valores_por_letra:
                valores_por_letra[letra].append(valor)
            else:
                valores_por_letra[letra] = [valor]

    # Construimos la lista de tuplas (letra, max, min), ordenada alfabéticamente por letra
    resultado = []
    for letra in sorted(valores_por_letra.keys()):
        max_valor = max(valores_por_letra[letra])
        min_valor = min(valores_por_letra[letra])
        resultado.append((letra, max_valor, min_valor))

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_05()
    print("Resultado:", resultado)
