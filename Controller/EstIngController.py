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
            prom = validar("Cual es su promedio actualmente\n", "flo")
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

    def devolverPrestamo():
        cc = validar("Ingrese su CC o seríal del computador:\n", "int") 
        flag = validarPrestamo(cc, 1)
        if flag:
            return "\nEste estudiante no tiene un préstamo registrado o el serial no hace parte de un préstamo\n"
        else: 

            for i in BDEstIng:
                if i.getCed() == cc or i.getSerial() == cc:
                    print (f"\nNombre del estudiante: {i.getNom()}\nCC: {i.getCed()}\nSerial computador prestado: {i.getSerial()}")
                    break
            dec = int(validar("Desea eliminar el préstamo\n1.SI\n2.NO\n", "int"))
            if dec == 1:                
                for i in BDEstIng:
                    if i.getCed() == cc or i.getSerial() == cc:
                        serial = i.getSerial()
                        BDEstIng.remove(i)
                        sobreEscribirBDEstIng(serial)
                        return f"\nEl préstamo del estudiante {i.getNom()} ha sido eliminado.\n"
            else:
                return "\nEl préstamo no ha sido eliminado"
            
    def modificarPrestamo():
        cc = validar("Ingrese su CC o serial del computador:\n", "int")
        flag = validarPrestamo(cc,1)
        if flag:
            return "\nEste estudiante no tiene un préstamo registrado o el serial no hace parte de un préstamo\n"
        else:
            for i in BDEstIng:
                if i.getCed() == cc or i.getSerial() == cc:
                    print (f"\nNombre del estudiante: {i.getNom()}\nCC: {i.getCed()}\nSerial computador prestado: {i.getSerial()}")
                    break
            dec = int(validar("¿Desea modificar el préstamo?\n1.SI\n2.NO\n", "int"))
            if dec == 1:
                while True:
                    dec2 = int(input(f"\n¿Cual dato desea modificar?\n1.Nombre\n2.Apellido\n3.Teléfono\n4.Semestre\n5.Promedio\n6.Serial del equipo\n"))
                    for i in BDEstIng:
                        if i.getCed() == cc or i.getSerial() == cc:
                            if dec2 == 1:
                                nombre = validar("\nIngrese el nuevo nombre:\n","str")
                                i.setNom(nombre)
                                
                            elif dec2 == 2:
                                apellido = validar("\nIngrese el nuevo apellido:\n","str")
                                i.setApe(apellido)
                    
                            elif dec2 == 3:
                                telefono = validar("\nIngrese el nuevo teléfono:\n","int")
                                i.setTel(telefono)
                                
                            elif dec2 == 4:
                                sem = validar("\nIngrese el nuevo semestre:\n","int")
                                i.setSem(sem)
                                
                            elif dec2 == 5:
                                prom = validar("\nIngrese el nuevo promedio:\n","flo")
                                i.setProm(prom)

                            elif dec2 == 6:
                                from CompController import CompController
                                disp = CompController.ListarDisp()
                                if disp != []:
                                    serial = validar(dato="comp")
                                    serial2 = i.getSerial()
                                    i.setSerial(serial)
                                    for i in BDComp:
                                        if serial == i.getSerial():
                                            i.setDisp(False)
                                    
                                    sobreEscribirBDEstIng(serial2)
                                else:
                                    return"\nLo siento no contamos con Tablets disponibles, intenta mas tarde\n"
                            else:
                                print("¡Porfavor ingrese una opcion válida!")
                                continue
                            sobreEscribirMod2()
                            return "\nEl préstamo se actualizó con éxito\n"
                            
                    break