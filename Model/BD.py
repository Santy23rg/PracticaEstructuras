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
pathEstIng = model_path / "EstIng.txt"

#Agregacion de rutas al sys
sys.path.append(str(controller_path))
sys.path.append(str(model_path))
##################################
from Tablet import * 
from Computador import * 
from EstudianteDis import EstudianteDis 
from EstudianteIng import EstudianteIng 

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

def actualizarBDEstIng():
    BDEstIng.clear()
    with open(pathEstIng, "r") as archivo:
        datos = {}
        for linea in archivo:
            text = linea.strip()
            if '-' in text:
                cc = datos['CC']
                nombre = datos['nombre']
                apellido = datos['apellido']
                telefono = datos['telefono']
                semestre = datos['semestre']
                promedio = datos['promedio']
                serial = datos['serial']
                EstIng = EstudianteIng(cc, nombre, apellido, telefono, semestre, promedio, serial)
                BDEstIng.append(EstIng)
                datos = {}
                continue
            dato = text.split(":")
            datos.update({dato[0] : dato[1].strip()})

actualizarBDEstIng()
            
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
    # Validación de datos flotantes                
        elif dato == "flo":
            while True:
                try:
                    data = input(f"\n{frase}")
                    data_float = float(data)
                    assert data_float > 0 and data_float <= 5
                    return str(data_float)
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
        
        elif dato == "comp":
            result = []
            while True:
                try:
                    from CompController import CompController
                    print("\nSeleccione el sistema operativo de su computador\nDisponibles:")
                    disponibles = CompController.ListarDisp()
                    index = 1
                    opcion = []
                    for i in disponibles:
                        print(f"{index}) {i}")
                        opcion.append([index, i])
                        index += 1
                    respuesta = validar(dato="int")
                    if int(respuesta) in range(1,index):
                        for i in opcion:
                            if i[0] == int(respuesta):
                                result=i[1]
                        index = 1
                        opcion = []
                        print("Escoja el procesador de su computador")
                        for k in BDComp:
                            if k.getSist() == result and k.getDisp():
                                print(f"{index}) {k.getProce()}")
                                opcion.append([index, k.getSerial()])
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
                    else:
                        print("Escoja una opcion dentro del rango")
                        continue
                except:
                    print(f"El dato ingresado no es válido, intente nuevamente!")    

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
        actualizarArchivoT(BDTablet)
    actualizarBDEstDis()  
    
def registrarEstIng(estudiante):
    path = model_path / "EstIng.txt"
    with open(path, 'a') as archivo:
        archivo.write(f"CC: {estudiante.getCed()}\n")
        archivo.write(f"nombre: {estudiante.getNom()}\n")
        archivo.write(f"apellido: {estudiante.getApe()}\n")
        archivo.write(f"telefono: {estudiante.getTel()}\n")
        archivo.write(f"semestre: {estudiante.getSem()}\n")
        archivo.write(f"promedio: {estudiante.getProm()}\n")
        archivo.write(f"serial: {estudiante.getSerial()}\n")
        archivo.write(f"--------------\n")
        for item in BDComp:
            if estudiante.getSerial() == item.getSerial():
                item.setDisp(False)
        actualizarArchivoC(BDComp)
    actualizarBDEstIng()        

# ACTUALIZAR ARCHIVO DE TABLETS
def actualizarArchivoT(BDTablet):
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

# ACTUALIZAR ARCHIVO DE COMPUTADORES
def actualizarArchivoC(BDComp):
    with open(compArch, 'w', encoding='utf-8') as archivo:
        for item in BDComp:
            archivo.write(f"serial: {item.getSerial()}\n")
            archivo.write(f"marca: {item.getMarca()}\n")
            archivo.write(f"tamaño: {item.getTamano()}\n")
            archivo.write(f"precio: {item.getPrecio()}\n")
            archivo.write(f"sistema: {item.getSist()}\n")
            archivo.write(f"procesador: {item.getProce()}\n")
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
    with open(pathEstDis, 'w') as archivo:
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
        actualizarArchivoT(BDTablet)

def sobreEscribirMod():
    with open(pathEstDis, 'w') as archivo:
        for estudiante in BDEstDis:
            archivo.write(f"CC: {estudiante.getCed()}\n")
            archivo.write(f"nombre: {estudiante.getNom()}\n")
            archivo.write(f"apellido: {estudiante.getApe()}\n")
            archivo.write(f"telefono: {estudiante.getTel()}\n")
            archivo.write(f"modalidad: {estudiante.getMod()}\n")
            archivo.write(f"asignaturas: {estudiante.getCantAsig()}\n")
            archivo.write(f"serial: {estudiante.getSerial()}\n")
            archivo.write(f"--------------\n")

def sobreEscribirBDEstIng(serial):
    with open(pathEstIng, 'w') as archivo:
        for estudiante in BDEstIng:
            archivo.write(f"CC: {estudiante.getCed()}\n")
            archivo.write(f"nombre: {estudiante.getNom()}\n")
            archivo.write(f"apellido: {estudiante.getApe()}\n")
            archivo.write(f"telefono: {estudiante.getTel()}\n")
            archivo.write(f"semestre: {estudiante.getSem()}\n")
            archivo.write(f"promedio: {estudiante.getProm()}\n")
            archivo.write(f"serial: {estudiante.getSerial()}\n")
            archivo.write(f"--------------\n")
        for i in BDComp:
            if i.getSerial() == serial:
                i.setDisp("disponible") 
        actualizarArchivoC(BDComp)

def sobreEscribirMod2():
    with open(pathEstIng, 'w') as archivo:
        for estudiante in BDEstIng:
            archivo.write(f"CC: {estudiante.getCed()}\n")
            archivo.write(f"nombre: {estudiante.getNom()}\n")
            archivo.write(f"apellido: {estudiante.getApe()}\n")
            archivo.write(f"telefono: {estudiante.getTel()}\n")
            archivo.write(f"semestre: {estudiante.getSem()}\n")
            archivo.write(f"promedio: {estudiante.getProm()}\n")
            archivo.write(f"serial: {estudiante.getSerial()}\n")
            archivo.write(f"--------------\n")
