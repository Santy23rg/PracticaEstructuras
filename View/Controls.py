from pathlib import Path
import sys

current_dir = Path(__file__).parent

model_path = current_dir / '../Model'
controller_path = current_dir / '../Controller'

sys.path.append(str(model_path))
sys.path.append(str(controller_path))

from EstDisController import *
from TabletController import * 
# MENUS

def mainMenu():
    print(f"{'-'*25}\n| Selecciona una Opcion |\n{'-'*25}")
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

def registrarPrestamoDis():
    disp = TabletController.ListarDisp()
    if disp != []:
        result = EstDisController.registrarPrestamo()
        print(result)
    else:
        print("\nLo siento no contamos con Tablets disponibles, intenta mas tarde\n")


def devolverPestamo2():
    result = EstDisController.devolverPrestamo()
    print(result)