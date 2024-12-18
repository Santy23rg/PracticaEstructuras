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
        for i in BDEstIng:
            if dato == i.getCed():
                for j in BDComp:
                    if j.getSerial() == i.getSerial():
                        return f"\n------\nSerial: {j.getSerial()}\nMarca: {j.getMarca()}\nTamaño: {j.getTamano()}\nPrecio: {j.getPrecio()}\nProcesador: {j.getProce()}\nSistema Op: {j.getSist()}\n\nSe encuentra en prestamo del estudiante:\nCC: {i.getCed()}\nNombre: {i.getNom()} {i.getApe()}\n------\n"
        for i in BDComp:
            if dato == i.getSerial():
                if i.getDisp(): 
                    return f"\n------\nSerial: {i.getSerial()}\nMarca: {i.getMarca()}\nTamaño: {i.getTamano()}\nPrecio: {i.getPrecio()}\nProcesador: {i.getProce()}\nSistema Op: {i.getSist()}\n\nSe encuentra disponible para prestamo\n"
                else:
                    for j in BDEstIng:
                        if i.getSerial() == j.getSerial():
                            return f"\n------\nSerial: {i.getSerial()}\nMarca: {i.getMarca()}\nTamaño: {i.getTamano()}\nPrecio: {i.getPrecio()}\nProcesador: {i.getProce()}\nSistema Op: {i.getSist()}\n\nSe encuentra en prestamo del estudiante:\nCC: {j.getCed()}\nNombre: {j.getNom()}\n------\n"
                    
                    
        
        return "\n-----\nNo se encuentra ningun Equipo con el criterio ingresado\n-----\n"
                
            

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
                return "\nEl préstamo no ha sido devuelto"
            
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
                    dec2 = int(validar(f"\n¿Cual dato desea modificar?\n1.Nombre\n2.Apellido\n3.Teléfono\n4.Semestre\n5.Promedio\n6.Serial del equipo\n", "int"))

                    if dec2 not in range(1, 7):
                        print("¡Porfavor ingrese una opción válida!")
                        continue

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
                            sobreEscribirMod2()
                            return "\nEl préstamo se actualizó con éxito\n"
            else:
                return "\nNo se modificó el prestamo\n"            