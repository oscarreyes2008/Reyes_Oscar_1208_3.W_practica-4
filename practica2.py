print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("Reyes Yañez Oscar Alonso-1208-3w:practica sobre español-ingles")
print(" ")#sirve para dejar un espacio a la hora de ejecutar

diccionario = {}# Crear un diccionario vacío para las traducciones
print(" ")#sirve para dejar un espacio a la hora de ejecutar
entrada = input("Ingrese las traducciones en formato 'español:inglés', separadas por comas: ")# Solicitar al usuario que ingrese las traducciones
pares = entrada.split(',')
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Llenar el diccionario con las traducciones
for par in pares:
    esp, ing = par.split(':')
    diccionario[esp.strip()] = ing.strip()  # Limpiar espacios
print(" ")#sirve para dejar un espacio a la hora de ejecutar
print("Diccionario de traducción:", diccionario)# Imprimir el diccionario resultante
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Solicitar una frase en español para traducir
frase = input("Ingrese una frase en español para traducir: ")
palabras = frase.split()  # Dividir la frase en palabras
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Traducir palabra por palabra
frase_traducida = []
for palabra in palabras:
    # Traducir usando el diccionario, o dejar la palabra original si no se encuentra
    traduccion = diccionario.get(palabra, palabra)
    frase_traducida.append(traduccion)
print(" ")#sirve para dejar un espacio a la hora de ejecutar
# Imprimir la frase traducida
print("Frase traducida:", ' '.join(frase_traducida))
print(" ")#sirve para dejar un espacio a la hora de ejecutar
