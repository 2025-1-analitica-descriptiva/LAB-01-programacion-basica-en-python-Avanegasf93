"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    # Ruta al archivo CSV
    ruta_archivo = "files/input/data.csv"
    
    # Diccionario para contar registros por mes
    conteo_meses = {}

    # Abrimos el archivo
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        for linea in file:
            # Limpiamos la línea y la separamos por tabulador
            partes = linea.strip().split("\t")

            # Obtenemos la fecha en formato YYYY-MM-DD
            fecha = partes[2]

            # Extraemos el mes, que son los caracteres del índice 5 al 7
            mes = fecha[5:7]

            # Acumulamos el conteo por mes
            if mes in conteo_meses:
                conteo_meses[mes] += 1
            else:
                conteo_meses[mes] = 1

    # Ordenamos los resultados por mes ('01', '02', ..., '12')
    resultado = sorted(conteo_meses.items())

    return resultado

# Ejecutar para probar
if __name__ == "__main__":
    resultado = pregunta_04()
    print("Resultado:", resultado)
