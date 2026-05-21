# Lista para guardar los nombres
nombres = []

# Cantidad de usuarios
cantidad = int(input("¿Cuántos usuarios deseas ingresar?: "))

# Ingresar nombres
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del usuario {i+1}: ")
    nombres.append(nombre)

# Ordenar alfabéticamente
nombres.sort()

# Mostrar resultados
print("\nNombres ordenados alfabéticamente:")
for nombre in nombres:
    print(nombre)