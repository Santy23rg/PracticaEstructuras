#Rutas Relativas
from pathlib import Path
import sys
current_dir = Path(__file__).parent

#Establecimiento de turas
compArch = current_dir / "InvComp.txt"
tabletArch = current_dir / "InvTablet.txt"
controller_path = current_dir / '../Controller'
model_path = current_dir / '../Model'
pathEstDis = model_path / "EstDis.txt"

#Agregacion de rutas al sys
sys.path.append(str(controller_path))
sys.path.append(str(model_path))
##################################
from Tablet import * 
from Computador import * 
from CompController import * 
from EstudianteDis import EstudianteDis 

BDTablet = []
BDComp = []
BDEstIng = []
BDEstDis = []


def actualizarBDEstDis():
    BDEstDis.clear()
    with open(pathEstDis, "r") as archivo:
        datos = {}
        for linea in archivo:
            text = linea.strip()
            if '-' in text:
                cc = datos['CC']
                nombre = datos['nombre']
                apellido = datos['apellido']
                telefono = datos['telefono']
                modalidad = datos['modalidad']
                asignatura = datos['asignaturas']
                serial = datos['serial']
                EstDis = EstudianteDis(cc, nombre, apellido, telefono, modalidad, asignatura, serial)
                BDEstDis.append(EstDis)
                datos = {}
                continue
            dato = text.split(":")
            datos.update({dato[0] : dato[1].strip()})

actualizarBDEstDis()
### Importacion de datos de inventario de Tablets
with open(tabletArch, 'r', encoding='utf-8') as archivo:
    datos = {}
    # Lee el contenido del archivo
    for linea in archivo:
        text = linea.strip()
        if '-' in text:
            serial = datos['serial']
            marca = datos['marca']
            tamano = datos['tamaño']
            precio = datos['precio']
            almac = datos['almacenamiento']
            peso = datos['peso']
            disp = True if datos['disp'].lower().strip() == "disponible" else False
            tablet = Tablet(serial, marca, tamano, precio, almac, peso, disp)
            BDTablet.append(tablet)
            datos = {}
            continue
        dato = text.split(":")
        datos.update({dato[0] : dato[1].strip()})

# Importacion de datos de inventario de Computadores
with open (compArch, 'r', encoding='utf-8') as archivo:
    datos = {}
    # Lee el contenido del archivo
    for linea in archivo:
        text = linea.strip()
        if '-' in text:
            serial = datos['serial']
            marca = datos['marca']
            tamano = datos['tamaño']
            precio = datos['precio']
            sistema = datos['sistema']
            procesador = datos['procesador']
            disp = True if datos['disp'].lower().strip() == "disponible" else False
            comp = Computador(serial, marca, tamano, precio, sistema, procesador, disp)
            BDComp.append(comp)
            datos = {}
            continue
        dato = text.split(":")
        datos.update({dato[0] : dato[1].strip()})

#Funcion de validacion de datos correctos
def validar(frase="", dato="str"):
    #Validacion de datos String
        if dato == "str":
            while True:
                try:
                    data = input(f"\n{frase}")
                    assert data.isalpha()
                    return data.strip()
                except:
                    print("El dato ingresado no es valido, Intente Nuevamente!")
    #Validacion de datos Int
        elif dato == "int":
            while True:
                try:
                    data = input(f"\n{frase}")
                    assert int(data) > 0 and data.isdigit()
                    return str(data)
                except:
                    print("El dato ingresado no es valido, Intente Nuevamente!")
    #Validacion para ingreso de semestre
        elif dato == "sem":
            while True:
                try:
                    data = input(f"\n{frase}")
                    assert int(data) > 0 and data.isdigit() and int(data) < 11
                    return str(data)
                except:
                    print("El dato ingresado no es valido, Intente Nuevamente!")
    #Validacion de datos de modalidad
        elif dato == "mod":
            while True:
                try:
                    data = input(f"\n{frase}1. Presencial\n2. Virtual\n")
                    if data == "1":
                        return "Presencial"
                    elif data == "2":
                        return "Virtual"
                    else:
                        print("El dato ingresado no es valido, Intente Nuevamente!")
                        continue
                        
                except:
                    print("El dato ingresado no es valido, Intente Nuevamente!")
        #Seleccion de tablet disponible
        elif dato == "tblt":
            while True:
                try:
                    from TabletController import TabletController
                    print("\nDe cuanto almacenamiento desea su tablet?\nDisponibles:")
                    disponibles = TabletController.ListarDisp()
                    index = 1
                    opcion = []
                    for i in disponibles:
                        print(f"{index}) {i.getAlmac()}")
                        opcion.append([index, i.getSerial()])
                        index += 1
                    respuesta = validar(dato="int")
                    if int(respuesta) in range(1,index):
                        for i in opcion:
                            if i[0] == int(respuesta):
                                result = i[1]
                                return result
                    else:
                        print("Escoja una opcion dentro del rango")
                        continue
                except:
                    print(f"El dato ingresado no es válido, intente nuevamente!")
        
        # elif dato == "comp":
        #     while True:
        #         try:
        #             from CompController import CompController
        #             print("\nDe cuanto almacenamiento desea su tablet?\nDisponibles:")
        #             disponibles = CompController.ListarDisp()
        #             for i in BDComp:
        #                 print(i.getDisp())
        #             index = 1
        #             opcion = []
        #             for i in disponibles:
        #                 print(f"{index}) {i.getAlmac()}")
        #                 opcion.append([index, i.getSerial()])
        #                 index += 1
        #             respuesta = validar(dato="int")
        #             if int(respuesta) in range(1,index+1):
        #                 for i in opcion:
        #                     if i[0] == int(respuesta):
        #                         result = i[1]
        #                         return result
        #             else:
        #                 print("Escoja una opcion dentro del rango")
        #                 continue
        #         except:
        #             print(f"El dato ingresado no es válido, intente nuevamente!")    

def registrarEstDis(estudiante):
    path = model_path / "EstDis.txt"
    with open(path, 'a') as archivo:
        archivo.write(f"CC: {estudiante.getCed()}\n")
        archivo.write(f"nombre: {estudiante.getNom()}\n")
        archivo.write(f"apellido: {estudiante.getApe()}\n")
        archivo.write(f"telefono: {estudiante.getTel()}\n")
        archivo.write(f"modalidad: {estudiante.getMod()}\n")
        archivo.write(f"asignaturas: {estudiante.getCantAsig()}\n")
        archivo.write(f"serial: {estudiante.getSerial()}\n")
        archivo.write(f"--------------\n")
        for item in BDTablet:
            if estudiante.getSerial() == item.getSerial():
                item.setDisp(False)
        actualizarArchivo(BDTablet)
    actualizarBDEstDis()        
                
def actualizarArchivo(BDTablet):
    with open(tabletArch, 'w', encoding='utf-8') as archivo:
        for item in BDTablet:
            archivo.write(f"serial: {item.getSerial()}\n")
            archivo.write(f"marca: {item.getMarca()}\n")
            archivo.write(f"tamaño: {item.getTamano()}\n")
            archivo.write(f"precio: {item.getPrecio()}\n")
            archivo.write(f"almacenamiento: {item.getAlmac()}\n")
            archivo.write(f"peso: {item.getPeso()}\n")
            archivo.write(f"disp: {'disponible' if item.getDisp() else False}\n")
            archivo.write(f"--------------\n")
            
def validarPrestamo(cc, tipoEst):
    if tipoEst == 2:    
        if not BDEstDis:
            return True
        else:
            for i in BDEstDis:
                if i.getCed() == cc or i.getSerial() == cc:
                    return False
            return True
    else:
        if not BDEstIng:
            return True
        else:
            for i in BDEstIng:
                if i.getCed() == cc or i.getSerial() == cc:
                    return False
            return True
        
def sobreEscribirBDEstDis(serial):
    with open(pathEstDis, 'w') as archivo:  # 'w' para sobreescribir el archivo
        for estudiante in BDEstDis:
            archivo.write(f"CC: {estudiante.getCed()}\n")
            archivo.write(f"nombre: {estudiante.getNom()}\n")
            archivo.write(f"apellido: {estudiante.getApe()}\n")
            archivo.write(f"telefono: {estudiante.getTel()}\n")
            archivo.write(f"modalidad: {estudiante.getMod()}\n")
            archivo.write(f"asignaturas: {estudiante.getCantAsig()}\n")
            archivo.write(f"serial: {estudiante.getSerial()}\n")
            archivo.write(f"--------------\n")
        for i in BDTablet:
            if i.getSerial() == serial:
                i.setDisp("disponible") 
        actualizarArchivo(BDTablet)