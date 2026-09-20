print("Bienvenido al programa de funciones en python.")

def informacion(nombre):
    print(f"Hola {nombre}, bienvenido al programa.")

informacion("Diana")

def actividad(despertar, desayuno, trabajo, estudio, cena, dormir):
    return f"Mi ultima actividad fue: {dormir}."

actividad_realizada = actividad("desperte a las 7:00 am", "desayune huevos con pan", "trabaje en la oficina", "estudie python", "cene arroz con pollo", "me fui a dormir a las 11:00 pm")
print(actividad_realizada)