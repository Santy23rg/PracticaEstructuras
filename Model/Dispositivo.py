from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, serial, marca, tamano, precio, disp):
        self._serial = serial
        self._marca = marca
        self._tamano = tamano
        self._precio = precio
        self._disp = disp

    def getSerial(self):
        return self._serial

    def getMarca(self):
        return self._marca

    def getTamano(self):
        return self._tamano
        
    def getPrecio(self):
        return self._precio

    def getDisp(self):
        return self._disp

    def setSerial(self, serial):
        self._serial=serial

    def setMarca(self, marca):
        self._marca=marca

    def setTamano(self, tamano):
        self._tamano=tamano
    
    def setPrecio(self, precio):
        self._precio=precio

    def setDisp(self, disp):
        self._disp=disp