#realizar un examen de 3 preguntas, el usuario debe responder con si o no y al final otorgarle una calificacion (la calificacion se logra con una variable que inicia en cero y por cada respuesta correcta incremente 1)

calificacion = 0

print("--- BIENVENIDO AL EXAMEN ---")
print("Por favor, responde las preguntas escribiendo 'SI' o 'NO'.\n")

# Pregunta 1
p1 = input("1. ¿El sol es una estrella? (SI/NO): ").strip().upper()
if p1 == "SI":
    calificacion += 1

# Pregunta 2
p2 = input("2. ¿Los cerdos pueden volar? (SI/NO): ").strip().upper()
if p2 == "NO":
    calificacion += 1

# Pregunta 3
p3 = input("3. ¿El agua hierve a los 100 grados Celsius a nivel del mar? (SI/NO): ").strip().upper()
if p3 == "SI":
    calificacion += 1

# Resultado final
print("\n----------------------------")
print(f"Examen terminado. Tu calificación final es: {calificacion} / 3")