from Estudiante import Estudiante

class EstudianteIng(Estudiante):
    def __init__(self, ced, nom, ape, tel, semestre, promedio, serial):
        super().__init__(ced, nom, ape, tel, serial)
        self.__semestre=semestre
        self.__promedio=promedio

    def getSem(self):
        return self.__semestre
    
    def getProm(self):
        return self.__promedio
    
    def setSem(self, sem):
        self.__semestre = sem
        
    def setProm(self, prom):
        self.__promedio = prom