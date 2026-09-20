#Funcion

# 1. Definimos la máquina (la función)
def mostrar_table(numero):
    for i in range(1, 11):
        resultado = i * numero
        print(numero, "x", i, "=", resultado)

# 2. Llamamos a la función (encendemos la máquina con diferentes números)
print("--- Tabla del 5 ---")
mostrar_table(5)

print("--- Tabla del 7 ---")
mostrar_table(7)