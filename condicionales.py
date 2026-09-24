#if condicionales
#Revisar si una condicion es mayor a 
balance = 500
if balance > 0:
    print("Puedes pagar")

#else que se realice en caso de que la condicion evaluada no se cumpla 
balance = 0
if balance > 0:
    print("Puedes pagar")
else:
    print("No tienes saldo suficiente")

#Likes 
likes = 200
if likes > 200:
    print("Excelente, 200 likes")
else:
    print("Casi llegas a los 200 likes")

#if con texto
lenguaje = "python"
if lenguaje == "python":
    print("Excelente decision")

lenguaje = "php"
if not lenguaje == "python":
    print("Excelente decision")

#Condicionales 
usuario_autenticado = True 

if usuario_autenticado == True:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")

#si un elemento existe o no en una lista
lenguajes = ["python", "kotlin", "java", "javascript"]
if "php" in lenguajes:
    print("php si existe")
else:
    print("no esta en la lista")

#if anidados 
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado == True:
    if usuario_admin == True:
        print("Acceso total")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesion")

#if elif else 
puntaje = 95
if puntaje >= 90:
    print("Excelente trabajo")
elif puntaje >= 80:
    print("Buen trabajo")
else:
    print("Necesitas mejorar")

