## Adivina la palabra
## Un proyecto hecho por Alejandro Buzón García y Álvaro Manuel Guerrero Ramos

# Librerias

import random

# Colores

class colors:
  RESET = "\n\x1b[0m"
  RED = "\n\x1b[31m"
  GREEN = "\n\x1b[32m"
  
# Variables

db = open("palabras_DB.txt", "r")  # Abrir el archivo de palabras (DATABASE)

palabras = db.readlines()  # Leer las palabras del archivo

palabra = random.choice(palabras)  # Elegir una palabra al azar

# Arregla los saltos de líneas y las ñ

palabra = palabra.replace("\n", "")
palabra = palabra.replace("Ã±", "ñ")

# Palabra introducida por el usuario

palabra_usuario = ""

palabras_nuevo = []

for i in palabras:
  palabras_nuevo.append(i.replace("\n", ""))
  palabras_nuevo.append(i.replace("Ã±", "ñ"))


def introducir_palabra():
  palabra_usuario_def = input("Introduce una palabra de cinco letras: ")
  if len(palabra_usuario_def) < 5:
    print("La palabra debe contener 5 letras")
    palabra_usuario = introducir_palabra()
  else:
    if palabra_usuario_def not in palabras_nuevo:
      print("La palabra introducida no se encuentra en la base de datos")
      palabra_usuario = introducir_palabra()
    else:
      return palabra_usuario_def


palabra_usuario = introducir_palabra()

# Lista de caracteres tanto como de palabra elegida al azar como de la palabra introducida por el usuario

palabra_lista = list(palabra)
palabra_usuario_lista = list(palabra_usuario)

# Código

# Comprobar si los carácteres de la palabra introducida por el usuario son correctos

print(palabra_usuario_lista)

def comprobar_caracteres(palabra_usuario_lista, palabra_lista):
  for i in palabra_usuario_lista:
    if i in palabra_lista:
      print(f"{i} está en la palabra")
    else:
      print(f"{i} no está en la palabra")


comprobar_caracteres(palabra_usuario_lista, palabra_lista)
