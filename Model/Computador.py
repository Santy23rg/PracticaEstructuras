from Dispositivo import *

class Computador(Dispositivo):
    def __init__(self, serial, marca, tamano, precio, sist, proce, disp):
    ##herencia de clase padre "Dispositivos"
        super().__init__(serial, marca, tamano, precio, disp)
        self._sist = sist
        self._proce = proce
    ##métodos específicos de la clase computador    
    def getSist(self):
        return self._sist

    def getProce(self):
        return self._proce

    def setSist(self, sist):
        self._sist=sist

    def setProce(self,proce):
        self._proce=proce
    

