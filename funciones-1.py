def informacion (nombre, puesto = "Desconocido", edad = 0):
    print(f"Soy {nombre}, tengo {edad} años y trabajo como {puesto}.")

informacion("Juan", "Ingeniero", 30)
informacion("Ana", "Diseñadora")
informacion("Luis", edad=25)