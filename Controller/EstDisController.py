from Imports import *

class EstDisController():
    
    # Método de registrar préstamo
    def registrarPrestamo():
        cc = validar("Ingrese su CC:\n", "int")
        flag = validarPrestamo(cc, 2)
        if flag:
            nom = validar("Ingrese su nombre:\n", "str")
            ape = validar("Ingrese su apellido:\n", "str")
            tel = validar("Ingrese su telefono:\n", "int")
            mod = validar("Cual es su modalidad:\n", "mod")
            asig = validar("Ingrese cantidad de asignaturas:\n", "int")
            serial = validar(dato="tblt")
            Est = EstudianteDis(cc, nom, ape, tel, mod, asig, serial)
            registrarEstDis(Est)
            return "\nPrestamo Registrado Correctamente\n"
        else:
            return "\nEste estudiante ya tiene un prestamo en la facultad, debe devolverlo antes de poder hacer otro prestamo\n"
        
    def devolverPrestamo():
        cc = validar("Ingrese su CC o seríal de la tablet:\n", "int") 
        flag = validarPrestamo(cc, 2)
        if flag:
            return "\nEste estudiante no tiene un prestamo registrado\n"
        else: 

            for i in BDEstDis:
                if i.getCed() == cc or i.getSerial() == cc:
                    print (f"Nombre del estudiante: {i.getNom()}\nCC: {i.getCed()}\nSerial tablet: {i.getSerial()}")
                    break
            dec = int(validar("Desea eliminar el prestamo\n1.SI\n2.NO\n", "int"))
            if dec == 1:                
                for i in BDEstDis:
                    if i.getCed() == cc or i.getSerial() == cc:
                        serial = i.getSerial()
                        BDEstDis.remove(i)
                        sobreEscribirBDEstDis(serial)
                        return f"\nEl prestamo del estudiante {i.getNom()} ha sido eliminado.\n"
            else:
                return "\nEl prestamo no ha sido eliminado"