import Estudiante


class EstudianteIng(Estudiante):
    def __init__(self, ced, nom, ape, tel, semestre, promedio, serial):
        super().__init__(ced, nom, ape, tel, serial)
        self.__semestre=semestre
        self.__promedio=promedio

    def RegistrarPrestamo():
        pass

    def ModificarPrestamo():
        pass

    def Devolucion():
        pass

    def BuscarEquipo():
        pass

    