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
