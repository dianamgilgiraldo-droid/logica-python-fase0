def evaluar_acceso(nombre, edad, tiene_membresia):
    # Evaluamos ambas condiciones juntas con and
    if edad >= 18 and tiene_membresia == True:
        print("Acceso concedido. ¡Bienvenid@,", nombre, "!")
    else:
        print("Acceso denegado. Se requiere ser mayor de edad y tener membresía activa para", nombre)


print("--- Caso 1: María (Mayor de edad con membresía) ---")
evaluar_acceso("Maria", 20, True)

print("--- Caso 2: Carlos (Menor de edad) ---")
evaluar_acceso("Carlos", 16, True)

print("--- Caso 3: Lucia (Mayor de edad sin membresía) ---")
evaluar_acceso("Lucia", 25, False)