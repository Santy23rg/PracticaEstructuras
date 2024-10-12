import Tablet

BDTablet = {}
BDComp = {}
BDEstIng = {}
BDEstDis = {}

#class Tablet():
    def __init__(self, serial, marca, tamano, precio, almac, peso, disp):
        self.__serial = serial
        self.__marca = marca
        self.__tamano = tamano
        self.__precio = precio
        self.__almac = almac
        self.__peso = peso
        self.__disp = disp
    
    def getSerial(self):
        return self.__serial
    def getMarca(self):
        return self.__marca
    def getTamano(self):
        return self.__tamano
    def getPrecio(self):
        return self.__precio
    def getAlmac(self):
        return self.__almac
    def getPeso(self):
        return self.__peso
    def getDisp(self):
        return self.__disp

with open('Model/Inv.txt', 'r', encoding='utf-8') as archivo:
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
            BDTablet.update({tablet.getSerial() : {
                "marca" : tablet.getMarca(),
                "tamaño" : tablet.getTamano(),
                "precio" : tablet.getPrecio(),
                "almacenamiento" : tablet.getAlmac(),
                "peso" : tablet.getPeso(),
                "disp" : tablet.getDisp(),
            }})
            datos = {}
            continue
        dato = text.split(":")
        datos.update({dato[0] : dato[1]})
    

    
        
