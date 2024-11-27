## Adivina la palabra
## Un proyecto hecho por Alejandro Buzón García y Álvaro Manuel Guerrero Ramos

# Librerias

import random

# Colores


class colors:
  RESET = "\x1b[0m"
  RED = "\x1b[31m"
  GREEN = "\x1b[32m"
  YELLOW = "\x1b[33m"


# Variables

# Intentos

tries = 0

# Archivo

db = open("palabras_DB.txt", "r")  # Abrir el archivo de palabras (DATABASE)

palabras = db.readlines()  # Leer las palabras del archivo

palabra = random.choice(palabras)  # Elegir una palabra al azar

# Arregla los saltos de líneas y las ñ

palabra = palabra.replace("\n", "")
palabra = palabra.replace("Ã±", "ñ")

# Palabra introducida por el usuario

palabras_nuevo = []

# Funciones de introducir palabras

for i in palabras:
  palabras_nuevo.append(i.replace("\n", ""))
  palabras_nuevo.append(i.replace("Ã±", "ñ"))


def introducir_palabra():
  palabra_usuario = input("Introduce una palabra de cinco letras: ")
  if len(palabra_usuario) < 5:
    print(f"{colors.RED}La palabra debe contener 5 letras{colors.RESET}")
    return introducir_palabra()
  else:
    if palabra_usuario not in palabras_nuevo:
      print(
          f"{colors.RED}La palabra introducida no se encuentra en la base de datos{colors.RESET}"
      )
      return introducir_palabra()
    else:
      return palabra_usuario


'''
palabra_usuario = introducir_palabra()

# Lista de caracteres tanto como de palabra elegida al azar como de la palabra introducida por el usuario

'''
palabra_lista = list(palabra)
'''
palabra_usuario_lista = list(palabra_usuario)

'''

# Código

# Comprobar si los carácteres de la palabra introducida por el usuario son correctos

def comprobar_caracteres(palabra_usuario_lista, palabra_lista):
  aciertos = 0
  print()
  for i in palabra_usuario_lista:
    if i in palabra_lista:
      if palabra_usuario_lista.index(i) == palabra_lista.index(i):
        print(f"{colors.GREEN}{i}{colors.RESET}", end="")
        aciertos += 1
      else:
        print(f"{colors.YELLOW}{i}{colors.RESET}", end="")
    else:
      print(f"{i}", end="")

  if aciertos == 5:
    print("Has ganado", end="\n")
    exit()

while (tries < 6):
  palabra_usuario = introducir_palabra()
  palabra_usuario_lista = list(palabra_usuario)
  comprobar_caracteres(palabra_usuario_lista, palabra_lista)
  print("\n")
  tries += 1   
