#Creando un diccionario simple 
#llave key

cancion = {
    "artista": "Metallica", #llave y valor
    "cancion": "Enter sandman",
    "lanzamiento": 1992,
    "likes": 3000
}

#Acceder a los elementos del diccionario
print(cancion["artista"])

#Mezclar con un string 
print(f"Estoy escuchando {cancion["artista"]} con la cancion {cancion["cancion"]}")

artista = cancion["artista"]
print(f"Estoy escuchando a {artista}")

#agregar nuevos valores 
cancion["playlist"] = "Rock"
print(cancion)

#Reemplazar valores
cancion["cancion"] = "Nothing else matters"
print(cancion)

#Eliminar un valor del diccionario 
del cancion["lanzamiento"]
print(cancion)
