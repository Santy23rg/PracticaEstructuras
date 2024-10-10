from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, serial, marc, tam, prec):
        self.__serial = serial
        self.__marc = marc
        self.__tam = tam
        self.__prec = prec

@abstractmethod
def getSerial():
    pass

@abstractmethod
def getMarc():
    pass

@abstractmethod
def getTam():
    pass

@abstractmethod
def getPrec():
    pass

@abstractmethod
def setSerial():
    pass

@abstractmethod
def setMarc():
    pass

@abstractmethod
def setTam():
    pass

@abstractmethod
def setPrec():
    pass