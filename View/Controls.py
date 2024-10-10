#MENUS
def mainMenu():
    print(f"{"-"*25}\n| Selecciona una Opcion |\n{"-"*25}")
    while True:
        try:
            respuesta = int(input("1. Ingenieria \n2. Diseño\n3. Imprimir Inventario\n4. Salir del Programa\n"))
            if respuesta in range(1,5):
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return respuesta

def SecMenu():
    print(f"{'-'*23}\n| Que deseas realizar |\n{'-'*23}")
    while True:
        try:
            respuesta = int(input("1. Registrar Prestamo de Equipo\n2. Modificar Prestamo\n3. Devolucion de Equipo\n4. Buscar Equipo\n5. Volver al menu principal\n"))
            if respuesta in range(1,6):
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return respuesta
