nombre = input("Cual es tu nombre: \r\n")
print(f"Hola {nombre}, bienvenido al programa.")

#Leer datos que seran numeros 
edad = input('cual es tu edad: \r\n')
#covertir edad a entero
edad = int(edad)

if edad >= 18:
    print('ya puedes votar')
else:
    print('aun no puedes votar')

#Mezclarlo con operadores 
numero = input('Agrega un numero y te dire si es par o impar \r\n')
numero = int(numero)

if numero % 2 == 0: #si el reciduo es cero significa que el numero es par
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')




