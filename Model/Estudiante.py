from abc import ABC, abstractmethod


class Estudiante(ABC):
    def __init__(self, ced, nom, ape, tel, serial):
        self.__ced = ced
        self.__nom = nom
        self.__ape = ape
        self.__tel = tel
        self.__serial = serial
    
    @abstractmethod
    def getCed():
        pass
    
    @abstractmethod
    def getNom():
        pass
    
    @abstractmethod
    def getApe():
        pass
    
    @abstractmethod
    def getTel():
        pass    
    
    @abstractmethod
    def getSerial():
        pass
    
    @abstractmethod
    def setCed():
        pass
    
    @abstractmethod
    def setNom():
        pass
    
    @abstractmethod
    def setApe():
        pass
    
    @abstractmethod
    def setTel():
        pass
    
    @abstractmethod
    def setSerial():
        pass
    

