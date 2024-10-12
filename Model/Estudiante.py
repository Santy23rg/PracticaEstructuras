from abc import ABC, abstractmethod


class Estudiante(ABC):
    def __init__(self, ced, nom, ape, tel, serial):
        self.__ced = ced
        self.__nom = nom
        self.__ape = ape
        self.__tel = tel
        self.__serial = serial
    
    @abstractmethod
    def getCed(self):
        return self.__ced
    
    @abstractmethod
    def getNom(self):
        return self.__nom
    
    @abstractmethod
    def getApe(self):
        return self.__ape
    
    @abstractmethod
    def getTel(self):
        return self.__tel
    
    @abstractmethod
    def getSerial(self):
        return self.__serial
    
    @abstractmethod
    def setCed(self, ced):
        self.__ced = ced
    
    @abstractmethod
    def setNom(self, nom):
        self.__nom = nom
    
    @abstractmethod
    def setApe(self, ape):
        self.__ape = ape
    
    @abstractmethod
    def setTel(self, tel):
        self.__tel = tel
        
    @abstractmethod
    def setSerial(self, serial):
        self.__serial = serial
    
    

