from Estudiante import Estudiante # se corrige la importacion porque "import Estudiante" hace de cuenta que es un modulo
def validar(frase, dato):
        if dato == "str":
            while True:
                try:
                    data = input(frase)
                    assert data.isalpha()
                    return data
                except:
                    print("Intenta nuevamente")
        elif dato == "int":
            while True:
                try:
                    data = int(input(frase))
                    return data
                except:
                    print("Intenta nuevamente")
        elif dato == "spec":
            while True:
                try:
                    data = input(frase)
                    assert data.lower() == "presencial" or data.lower() == "virtual"
                    return data
                except:
                    print("Intenta nuevamente")

class EstudianteDis(Estudiante):  # Hereda de Estudiante
    def __init__(self, ced, nom, ape, tel, modEst, cantAsig, serial):
        super().__init__(ced, nom, ape, tel, serial)  # Llama al constructor de la clase padre
        self.__modEst = modEst  # Variable para modalidad de estudio
        self.__cantAsig = cantAsig  # Variable para cantidad de asignaturas

    # Implementación de métodos abstractos
    def getCed(self):
        return super().getCed()

    def getNom(self):
        return super().getNom()

    def getApe(self):
        return super().getApe()

    def getTel(self):
        return super().getTel()

    def getSerial(self):
        return super().getSerial()

    def setCed(self, ced):
        super().setCed(ced)

    def setNom(self, nom):
        super().setNom(nom)

    def setApe(self, ape):
        super().setApe(ape)

    def setTel(self, tel):
        super().setTel(tel)

    def setSerial(self, serial):
        super().setSerial(serial)

    
            

    # Método de registrar préstamo
    def RegistrarPrestamo(self):

        cc = validar("ingrese su cc:", "int")
        nom = validar("ingrese su nom:", "str")
        ape = validar("ingrese su ape:", "str")
        tel = validar("ingrese su tel:", "int")
        mod = validar("cual es su modalidad (presencial/virtual)", "spec")
        asig = validar("ingrese cantidad de asignatura:", "int")

        print(f"sus datos son {cc} y {nom} y {ape} y {tel} y {mod}")

       
    def ModificarPrestamo(self):
        pass

    def DevolucionEquipo(self):
        pass

    def BuscarEquipo(self):
        pass
estudiante1 = EstudianteDis("", "", "", "", "", 0, "")
estudiante1.RegistrarPrestamo()