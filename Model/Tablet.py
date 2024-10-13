from Dispositivo import *

class Tablet(Dispositivo):
    def __init__(self, serial, marca, tamano, precio, almac, peso, disp):
        super().__init__(serial,marca, tamano,precio, disp)
        self._almac = almac
        self._peso = peso

    def getAlmac(self):
        return self._almac
        
    def getPeso(self):
        return self._peso
    
    def getAlmc(self, almac):
        self._almac=almac

    def getPeso(self, peso):
        self._peso=peso

dis = Tablet("001","s","10","11","123","33",True)

dis.setMarca("Lenovo")
print(dis.getMarca())