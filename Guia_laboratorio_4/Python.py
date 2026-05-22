while True:

    print("\n========= MENÚ =========")
    print("1. Manipulación de texto")
    print("2. Buscar edad por nombre")
    print("3. Buscar usuarios por ciudad")
    print("4. Ordenar nombres")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # OPCIÓN 1: MANIPULACIÓN DE TEXTO
    if opcion == "1":

        #Declarar una cadena de texto
        texto = "Python es un lenguaje de programación muy popular"

        print("\nTexto original:")
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

    # OPCIÓN 2: BUSCAR EDAD
    elif opcion == "2":

        #Listas paralelas
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

    # OPCIÓN 3: BUSCAR USUARIOS POR CIUDAD
    elif opcion == "3":
    
        # Creación de Diccionarios 
        usuarios = [
            {
                "nombre": "Jhordy",
                "email": "Jhordy24@gmail.com",
                "ciudad": "Cajamarca"
            },
            {
                "nombre": "Luis",
                "email": "Luis@gmail.com",
                "ciudad": "Trujillo"
            },
            {
                "nombre": "Carlos",
                "email": "carl0s@gmail.com",
                "ciudad": "Lima"
            },
            {
                "nombre": "María",
                "email": "maria@gmail.com",
                "ciudad": "Piura"
            }
        ]

        # Búsqueda textual por ciudad
        buscar_ciudad = "Lima"
        
        print("\nUsuarios de la ciudad:", buscar_ciudad)

        for usuario in usuarios:
            if usuario["ciudad"].lower() == buscar_ciudad.lower():
                print(usuario["nombre"], "-", usuario["email"])


    # OPCIÓN 4: ORDENAR NOMBRES
    elif opcion == "4":

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


    # OPCIÓN 5: SALIR
    elif opcion == "5":

        print("\nPrograma finalizado.")
        break

    # OPCIÓN INVÁLIDA
    else:
        print("\nOpción inválida. Intente nuevamente.")

