from Dispositivo import Dispositivo

class Tablet(Dispositivo):
    def __init__(self, serial, marca, tamano, precio, almac, peso, disp):
    ##herencia de clase padre "Dispositivos"
        super().__init__(serial,marca, tamano,precio, disp)
        self._almac = almac
        self._peso = peso
        
    ##métodos específicos de la clase tablet    
    def getAlmac(self):
        return self._almac
        
    def getPeso(self):
        return self._peso
    
    def setAlmc(self, almac):
        self._almac=almac

    def setPeso(self, peso):
        self._peso=peso
        