## Adivina la palabra
## Un proyecto hecho por Alejandro Buzón García y Álvaro Manuel Guerrero Ramos 2º BTO B IES La Fuensanta
# Librerias
import random
# Colores
class colors:
  # Aquí tenemos para seleccionar el color de la letra :D
  RESET = "\x1b[0m"
  RED = "\x1b[31m"
  GREEN = "\x1b[32m"
  YELLOW = "\x1b[33m"
# Juego base
def juego():
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
  palabras_nuevo = [
  ]  # No sé para qué sirve la verdad pero sé que es nesesario :(
  for i in palabras:
    # Reemplazamos los carácteres especiales
    palabras_nuevo.append(i.replace("\n", ""))
    palabras_nuevo.append(i.replace("Ã±", "ñ"))
  # Función que le pide al usuario que introduzca una palabra
  def introducir_palabra():
    # Le pedimos al usuario que introduzca una palabra
    palabra_usuario = input("Introduce una palabra de cinco letras: ")
    # Comprobamos que la palabra introducida tenga cinco letras sin tildes
    if len(palabra_usuario) < 5 or len(palabra_usuario) > 5:
      print(
          f"{colors.RED}La palabra debe contener 5 letras y sin tildes{colors.RESET}"
      )
      return introducir_palabra()
    else:
      # Comprobamos que la palabra introducida esté en el archivo
      if palabra_usuario not in palabras_nuevo:
        print(
            f"{colors.RED}La palabra introducida no se encuentra en la base de datos{colors.RESET}"
        )
        return introducir_palabra()
      else:
        # Si todo está bien, devolvemos la palabra introducida
        return palabra_usuario
  # Lista de caracteres de la palabra
  palabra_lista = list(palabra)
  # Comprobar si los carácteres de la palabra introducida por el usuario son correctos
  #! Print de pruebas no hagas trampa pillín ;)
  #! <print(palabra)>
  # Función que comprueba los caracteres de la palabra introducida por el usuario y los compara con la palabra elegida al azar
  # Esta función es una fumada de código, pero funciona que es lo importante :D
  def comprobar_caracteres(palabra_usuario_lista, palabra_lista):
    # Variables de la funcion
    comprobacion = [
        "x", "x", "x", "x", "x"
    ]  # Lista de caracteres donde vamos a guardar el resultado de la comprobación
    aciertos = 0  # Contador de aciertos
    contador = {}  # Diccionario para contar las letras
    for i in palabra_lista:
      contador[i] = contador.get(i, 0) + 1
    # Empieza la comprobación
    for i in range(5):
      # Contamos primeros cuales letras están en su posición adecuada y la añadimos a la lista con el color verde
      if palabra_usuario_lista[i] == palabra_lista[i]:
        comprobacion[
            i] = f"{colors.GREEN}{palabra_usuario_lista[i]}{colors.RESET}"
        aciertos += 1
        contador[palabra_usuario_lista[i]] -= 1
      else:
        # Excluimos aquí las demás letras que pueden que estén en la palabra
        comprobacion[i] = f"{palabra_usuario_lista[i]}"
    for i in range(5):
      # Contamos cuales letras están en la palabra pero no en su posición adecuada y las añadimos a la lista con el color amarillo
      if palabra_usuario_lista[i] in palabra_lista and contador[
          palabra_usuario_lista[i]] > 0 and palabra_lista[
              i] != palabra_usuario_lista[i]:
        comprobacion[
            i] = f"{colors.YELLOW}{palabra_usuario_lista[i]}{colors.RESET}"
        contador[palabra_usuario_lista[i]] -= 1
    # Imprimir la comprobación al usuario
    for i in range(5):
      print(comprobacion[i], end="")
    # Si aciertos es igual a 5, hemos acertado la palabra
    if aciertos == 5:
      print("\nHas ganado")
      qplay = input("¿Quieres jugar de nuevo? (s/n): ")
      if qplay == "s":
        juego()
      else:
        exit()
  # Un bucle que se ejecuta siempre que no se ha acertado la palabra y que se han hecho menos de 6 intentos
  while tries < 6:
    palabra_usuario = introducir_palabra()
    palabra_usuario_lista = list(palabra_usuario)
    comprobar_caracteres(palabra_usuario_lista, palabra_lista)
    print("\n")
    tries += 1
  # Si has agotado todos tus intentos
  if tries == 6:
    print(f"Has perdido, la palabra era {palabra}")
    qplay = input("¿Quieres jugar de nuevo? (s/n): ")
    if qplay == "s":
      juego()
    else:
      exit()
## INICIALIZAR JUEGO
juego()
