#While: se ejecuta siempre y cuando la condicion sea verdadera, si es falsa no se ejecuta

numero = 0

# while numero <= 10:
#     print(numero)
#     numero += 1 #incremento de numero en 1 

#If dentro del while

while numero <= 10:
    if numero == 5:
        print('Cincooo!!')
    else:
        print(numero)
    numero += 1 #incremento de numero en 1 

while numero <= 10:
    if numero == 5:
        break #rompe el ciclo y sale del while 
    else:
        print(numero)
    numero += 1 #incremento de numero en 1     
