class Estudiante():
    def __init__(self, ced, nom, ape, tel, serial):
        self.__ced = ced
        self.__nom = nom
        self.__ape = ape
        self.__tel = tel
        self.__serial = serial
    
    
    def getCed(self):
        return self.__ced
    
    
    def getNom(self):
        return self.__nom
    
    
    def getApe(self):
        return self.__ape
    
    
    def getTel(self):
        return self.__tel
    
    
    def getSerial(self):
        return self.__serial
    
    
    def setCed(self, ced):
        self.__ced = ced
    
    
    def setNom(self, nom):
        self.__nom = nom
    
    
    def setApe(self, ape):
        self.__ape = ape
    
    
    def setTel(self, tel):
        self.__tel = tel
        
    
    def setSerial(self, serial):
        self.__serial = serial
    
    

