from Controls import *


while True:
    respuesta = mainMenu()
    
    #OPCION 1
    if respuesta == 1:
        
        respuesta = SecMenu()
        if respuesta == 1:
            registrarPrestamoIng()
        elif respuesta == 2:
            modificarPrestamoIng()
        elif respuesta == 3:
            devolverPestamoIng()
        elif respuesta == 4:
            buscarEquipoIng()
        elif respuesta == 5:
            continue
        
    #OPCION 2
    elif respuesta == 2:
        respuesta = SecMenu()
        if respuesta == 1:
            registrarPrestamoDis()
        elif respuesta == 2:
            modificarPrestamoDis()
        elif respuesta == 3:
            devolverPestamoDis()
        elif respuesta == 4:
            pass
        elif respuesta == 5:
            continue
    
    #OPCION 3
    elif respuesta == 3:
        mostrarInventario()
    
    #OPCION 4
    elif respuesta == 4:
        break

                    
