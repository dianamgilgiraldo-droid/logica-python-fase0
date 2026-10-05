#crear una aplicacion de playlist de musica
playlist = {} #Diccionario vacio para almacenar canciones
playlist['canciones'] = [] #Lista vacia de canciones


# Funcion principal 
def app ():

    #Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input ('¿Como desea nombrrar la playlist?: \r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            
            #ya se tiene un nombre, se elimina el true para salir del bucle
            agregar_playlist = False  

            #mandar llamar la funcion para agregar canciones 
            agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones a la playlist 
    agregar_cancion = True

    while agregar_cancion:
        #Preguntar al usuario que cacncion desean agregar 
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == 'X':
            #Dejar de agregar canciones, se cambia bandera a false para salir del bucle 
            #Agregar elementos a una lista .append()
            print('Fianlizado...')
        else:
            #Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)

app()