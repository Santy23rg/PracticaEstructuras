from pathlib import Path
import sys

current_dir = Path(__file__).parent

model_path = current_dir / '../Model'
controller_path = current_dir / '../Controller'

sys.path.append(str(model_path))
sys.path.append(str(controller_path))

from EstDisController import *
from EstIngController import *
from TabletController import * 
from CompController import * 
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
        
def registrarPrestamoIng():
    disp = CompController.ListarDisp()
    if disp != []:
        result = EstIngController.registrarPrestamo()
        print(result)
    else:
        print("\nLo siento no contamos con Computadores disponibles, intenta mas tarde\n")

def buscarEquipoIng():
    dato = input("Ingrese CC del estudiante o Serial del equipo:\n")
    EstIngController.buscarEquipo(dato)

def devolverPestamoDis():
    result = EstDisController.devolverPrestamo()
    print(result)

def mostrarInventario():
    # Rutas a los archivos de inventario
    comp_path = current_dir / '../Model/InvComp.txt'
    tablet_path = current_dir / '../Model/InvTablet.txt'

    # Leer e imprimir inventario de computadores
    print(f"\n{'-'*30}\n| INVENTARIO COMPUTADORES |\n{'-'*30}")
    with comp_path.open('r', encoding='utf-8') as comp:
        dispositivo = {}
        for line in comp:
            if line.strip() == "--------------":
                # Muestra el dispositivo solo si está disponible
                if dispositivo.get("disp") == "disponible":
                    # Imprime todos los atributos excepto "disp"
                    for i, valor in dispositivo.items():
                        if i != "disp":
                            print(f"{i}: {valor}")
                    print("-" * 20) # separa cada dispositivo
                dispositivo = {}
            elif line:
                i, valor = line.split(": ", 1)
                dispositivo[i.strip()] = valor.strip()

    # Leer e imprimir inventario de tablets
    print(f"\n{'-'*30}\n| INVENTARIO TABLETS |\n{'-'*30}")
    with tablet_path.open('r', encoding='utf-8') as tablet:
        dispositivo = {}
        for line in tablet:
            if line.strip() == "--------------": 
                # Muestra el dispositivo solo si está disponible
                if dispositivo.get("disp") == "disponible":
                    # Imprime todos los atributos excepto "disp"
                    for i, valor in dispositivo.items():
                        if i != "disp":
                            print(f"{i}: {valor}")
                    print("-" * 20) # separa cada dispositivo
                dispositivo = {}
            elif line:
                i, valor = line.split(": ", 1)
                dispositivo[i.strip()] = valor.strip()


def modificarPrestamoDis():
    result = EstDisController.modificarPrestamo()
    print(result)

def modificarPrestamoIng():
    result = EstIngController.modificarPrestamo()
    print(result)

def devolverPestamoIng():
    result = EstIngController.devolverPrestamo()
    print(result)

