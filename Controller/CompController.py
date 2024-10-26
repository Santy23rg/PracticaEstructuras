from Imports import *

class CompController():
    
    def ListarDisp():
        disponibles = []
        for item in BDComp:
            if item.getDisp():
                if disponibles.count(item.getSist()) < 1:
                    disponibles.append(item.getSist())
        return disponibles
    