from Estudiante import Estudiante # se corrige la importacion porque "import Estudiante" hace de cuenta que es un modulo

class EstudianteDis(Estudiante):  # Hereda de Estudiante
    def __init__(self, ced, nom, ape, tel, modEst, cantAsig, serial):
        super().__init__(ced, nom, ape, tel, serial)  # Llama al constructor de la clase padre
        self.__modEst = modEst  # Variable para modalidad de estudio
        self.__cantAsig = cantAsig  # Variable para cantidad de asignaturas

    def getMod(self):
        return self.__modEst
    
    def getCantAsig(self):
        return self.__cantAsig
    
    def setMod(self, mod):
        self.__modEst = mod

    def setCantAsig(self, cant):
        self.__cantAsig = cant
    
            

    