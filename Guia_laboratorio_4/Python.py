#Declarar una cadena de texto

texto = "Python es un lenguaje de programación muy popular"

print("Texto original:")
print(texto)

#1. Obtener una subcadena
subcadena = texto[0:6]

print("\nSubcadena:")
print(subcadena)

#2.Buscar una palabra específica
buscar = texto.find("lenguaje")
print("\nPosición de la palabra 'lenguaje':")
print(buscar)

#3 Reemplazar una palabra por otra
nuevo_texto = texto.replace("popular", "potente")
print("\nTexto reemplazado:")
print(nuevo_texto)

#4 Separar el texto en partes
partes = texto.split()
print("\nTexto separado en palabras:")
print(partes)