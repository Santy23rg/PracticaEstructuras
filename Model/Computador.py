from Dispositivo import *

class Computador(Dispositivo):
    def __init__(self, serial, marca, tamano, precio, sist, proce, disp):
        super().__init__(serial, marca, tamano, precio, disp)
        self._sist = sist
        self._proce = proce
    
    def getSist(self):
        return self._sist

    def getProce(self):
        return self._proce

    def setSist(self, sist):
        self._sist=sist

    def setProce(self,proce):
        self._proce=proce
    

dis = Computador("001","s","10","11","a","z",True)
print(dis.getDisp())
