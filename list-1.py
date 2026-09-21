lenguajes = ["python", "java", "c++", "javascript", "html", "css"]

print(lenguajes)

print(lenguajes[0]) #Acceder al primer elemento de la lista 

#Ordenar los lementos 
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendi {lenguajes[3]}"

#Modificando valores de un arreglo 
lenguajes[2] = "php"
print(lenguajes)

#agregar elementos a un arreglo 
lenguajes.append("Rubi")
print(lenguajes)

#Eliminar un producto
del lenguajes[1]
print(lenguajes)

#Eliminar de un arreglo o list
lenguajes.pop()
print(lenguajes)

#Eliminar con pop una posicion en especifico 
lenguajes.pop(0)
print(lenguajes)

#Eliminar por nombre 
lenguajes.remove("php")
print(lenguajes)

#arreglo o lista con 100 elementos para ello se utiliza los iteradores, para correr el mimso codigo hasta que se cumpla el total de una tarea 
lenguajes =  ["python", "java", "c++", "javascript", "html", "css"]
for lenguaje in lenguajes:
    #print(lenguaje)
    print(f"estoy aprendiendo {lenguaje}")

# For que escriba numeros, tres salta de tres en tres 
for numero in range(1, 11, 3):
    print(numero)

