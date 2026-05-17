nombres = ["Ana", "Luis", "Carlos", "María"]
edades = [20, 25, 30, 22]

# Nombre a buscar
buscar_nombre = "Carlos"

# Buscar la persona y mostrar su edad
if buscar_nombre in nombres:
    indice = nombres.index(buscar_nombre)
    print("La edad de", buscar_nombre, "es:", edades[indice])
else:
    print("Persona no encontrada")