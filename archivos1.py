def app():

    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip()) #rstrip() elimina los espacios en blanco al final de la linea

app()