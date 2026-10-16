def app():
    #Crear el archivo
    archivo = open('archivo.txt', 'w') #w es modo esxritura y si no existe lo creara, si existe lo sobreescribe

    #Generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea' + str(i) + '\r\n') # \r\n es salto de linea en windows, en linux es \n

    #Cerrar el archivo
    archivo.close()

app()