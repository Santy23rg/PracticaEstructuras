from Imports import *

class TabletController():
    
    def ListarDisp():
        disponibles = [item for item in BDTablet if item.getDisp()]
        return disponibles
