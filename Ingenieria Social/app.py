import googlesearch

def realizar_busqueda(objetivo):
    resultados = []

    # Realizar búsquedas en Google
    resultados = googlesearch.search(objetivo, num_results=5)

    return resultados


def guardar_resultados_en_archivo(resultados, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for resultado in resultados:
            archivo.write(resultado + '\n')

if __name__ == "__main__":
    # Introduce el objetivo
    objetivo = input("Introduce el objetivo de la búsqueda: ")

    # Realiza la búsqueda
    resultados = realizar_busqueda(objetivo)

    # Guarda los resultados en un archivo de texto
    nombre_archivo = "resultados_busqueda.txt"
    guardar_resultados_en_archivo(resultados, nombre_archivo)

    print(f"Los resultados de la búsqueda se han guardado en {nombre_archivo}")
