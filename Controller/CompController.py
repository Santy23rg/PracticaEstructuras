from Imports import *

class CompController():
    
    def ListarDisp():
        disponibles = [item for item in BDComp if item.getDisp()]
        return disponibles