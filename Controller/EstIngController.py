from Imports import *

class EstIngController():
    
    # Método de registrar préstamo
    def registrarPrestamo():
        cc = validar("Ingrese su CC:\n", "int")
        flag = validarPrestamo(cc, 1)
        if flag:
            nom = validar("Ingrese su nombre:\n", "str")
            ape = validar("Ingrese su apellido:\n", "str")
            tel = validar("Ingrese su telefono:\n", "int")
            sem = validar("Que semestre esta cursando:\n", "sem")
            prom = validar("Cual es su promedio actualmente\n", "int")
            serial = validar(dato="comp")
            Est = EstudianteIng(cc, nom, ape, tel, sem, prom, serial)
            registrarEstIng(Est)
            return "\nPrestamo Registrado Correctamente\n"
        else:
            return "\nEste estudiante ya tiene un prestamo en la facultad, debe devolverlo antes de poder hacer otro prestamo\n"
        
    def buscarEquipo(dato):
        pass
        # for i in BDEstIng:
        #     if i.getCed() == dato or i.getSerial() == dato:
        #         serial = i.getSerial()
        #         print(f"\nPRESTAMO\nCC: {i.getCed()}\nNombre: {i.getNom()}")
        #         break
        # for i in BDComp:
        #     if i.getSerial() == dato:
        #         print(f"Marca: {i.getMarca()}\nSistema: {i.getSist()}\nProcesador: {i.getProce()}")
        #         break