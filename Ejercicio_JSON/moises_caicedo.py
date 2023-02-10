import json

# Crear objeto JSON a partir de un diccionario de Python
jugador = {"nombres": "Moises", "apellidos": "Caicedo", 
"fecha_nacimiento": "02-11-2001", "edad": 21, "pais_nacimiento": "Ecuador", "ciudad": "Santo Domingo", 
"posición": "Mediocampista", "grupo_sanguíneo": "AB+", "nacionalidad": "Ecuatoriana"}

# Guardar objeto JSON en un archivo
with open("moises_caicedo.json", "w") as file:
    json.dump(jugador, file)

# Cargar objeto JSON desde un archivo
with open("moises_caicedo.json", "r") as file:
    jugador = json.load(file)

# Acceder a los valores
print("Nombres:", jugador["nombres"])
print("Apellidos:", jugador["apellidos"])
print("Fecha de nacimiento:", jugador["fecha_nacimiento"])
print("Edad:", jugador["edad"])
print("País de nacimiento:", jugador["pais_nacimiento"])
print("Ciudad:", jugador["ciudad"])
print("Posición:", jugador["posición"])
print("Grupo sanguíneo:", jugador["grupo_sanguíneo"])
print("Nacionalidad:", jugador["nacionalidad"])
