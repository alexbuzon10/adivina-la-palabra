import random

db = open("palabras_DB.txt", "r")

palabras = db.readlines()

palabra = random.choice(palabras)

palabra = palabra.replace("\n", "")
palabra = palabra.replace("Ã±", "ñ")

print(palabra)

