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
            return "\nEste estudiante ya tiene un préstamo en la facultad, debe devolverlo antes de poder hacer otro préstamo\n"
        
    def devolverPrestamo():
        cc = validar("Ingrese su CC o seríal de la tablet:\n", "int") 
        flag = validarPrestamo(cc, 2)
        if flag:
            return "\nEste estudiante no tiene un préstamo registrado o el serial no hace parte de un préstamo\n"
        else: 

            for i in BDEstDis:
                if i.getCed() == cc or i.getSerial() == cc:
                    print (f"\nNombre del estudiante: {i.getNom()}\nCC: {i.getCed()}\nSerial tablet prestada: {i.getSerial()}")
                    break
            dec = int(validar("Desea eliminar el préstamo\n1.SI\n2.NO\n", "int"))
            if dec == 1:                
                for i in BDEstDis:
                    if i.getCed() == cc or i.getSerial() == cc:
                        serial = i.getSerial()
                        BDEstDis.remove(i)
                        sobreEscribirBDEstDis(serial)
                        return f"\nEl préstamo del estudiante {i.getNom()} ha sido eliminado.\n"
            else:
                return "\nEl préstamo no ha sido eliminado"
            
    def modificarPrestamo():
        cc = validar("Ingrese su CC o serial de la tablet:\n", "int")
        flag = validarPrestamo(cc,2)
        if flag:
            return "\nEste estudiante no tiene un préstamo registrado o el serial no hace parte de un préstamo\n"
        else:
            for i in BDEstDis:
                if i.getCed() == cc or i.getSerial() == cc:
                    print (f"\nNombre del estudiante: {i.getNom()}\nCC: {i.getCed()}\nSerial tablet prestada: {i.getSerial()}")
                    break
            dec = int(validar("¿Desea modificar el préstamo?\n1.SI\n2.NO\n", "int"))
            if dec == 1:
                while True:
                    dec2 = int(input(f"\n¿Cual dato desea modificar?\n1.Nombre\n2.Apellido\n3.Teléfono\n4.Modalidad de estudio\n5.Cantidad de asignaturas que está viendo\n6.Serial del equipo\n"))
                    for i in BDEstDis:
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
                                mod = validar("\nIngrese la nueva modalidad de estúdio:\n","mod")
                                i.setMod(mod)
                                
                            elif dec2 == 5:
                                asig = validar("\nIngrese la nueva cantidad de asignaturas:\n","int")
                                i.setCantAsig(asig)
                            
                            elif dec2 == 6:
                                from TabletController import TabletController
                                disp = TabletController.ListarDisp()
                                if disp != []:
                                    serial = validar(dato="tblt")
                                    serial2 = i.getSerial()
                                    i.setSerial(serial)
                                    for i in BDTablet:
                                        if serial == i.getSerial():
                                            i.setDisp(False)
                                    
                                    sobreEscribirBDEstDis(serial2)
                                else:
                                    return"\nLo siento no contamos con Tablets disponibles, intenta mas tarde\n"

                            else:
                                print("¡Porfavor ingrese una opcion válida!")
                                continue
                            sobreEscribirMod()
                            return "\nEl préstamo se actualizó con éxito\n"
                            
                    break
            else:
                return "\nNo se modificó el prestamo\n"