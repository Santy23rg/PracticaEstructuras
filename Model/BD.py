from Tablet import *
from Computador import *

from pathlib import Path
import sys

current_dir = Path(__file__).parent
compArch = current_dir / "InvComp.txt"
tabletArch = current_dir / "InvTablet.txt"

BDTablet = {}
BDComp = {}
BDEstIng = {}
BDEstDis = {}

### Importacion de datos de inventario de Tablets
with open(tabletArch, 'r', encoding='utf-8') as archivo:
    datos = {}
    # Lee el contenido del archivo
    for linea in archivo:
        text = linea.strip()
        if '-' in text:
            serial = datos['serial']
            marca = datos['marca']
            tamano = datos['tamaño']
            precio = datos['precio']
            almac = datos['almacenamiento']
            peso = datos['peso']
            disp = True if datos['disp'].lower().strip() == "disponible" else False
            tablet = Tablet(serial, marca, tamano, precio, almac, peso, disp)
            BDTablet.update({tablet.getSerial() : {
                "marca" : tablet.getMarca(),
                "tamaño" : tablet.getTamano(),
                "precio" : tablet.getPrecio(),
                "almacenamiento" : tablet.getAlmac(),
                "peso" : tablet.getPeso(),
                "disp" : tablet.getDisp(),
            }})
            datos = {}
            continue
        dato = text.split(":")
        datos.update({dato[0] : dato[1]})
    
# Importacion de datos de inventario de Computadores
with open (compArch, 'r', encoding='utf-8') as archivo:
    datos = {}
    # Lee el contenido del archivo
    for linea in archivo:
        text = linea.strip()
        if '-' in text:
            serial = datos['serial']
            marca = datos['marca']
            tamano = datos['tamaño']
            precio = datos['precio']
            sistema = datos['sistema']
            procesador = datos['procesador']
            disp = True if datos['disp'].lower().strip() == "disponible" else False
            comp = Computador(serial, marca, tamano, precio, sistema, procesador, disp)
            BDComp.update({comp.getSerial() : {
                "marca" : comp.getMarca(),
                "tamaño" : comp.getTamano(),
                "precio" : comp.getPrecio(),
                "sistema" : comp.getSist(),
                "procesador" : comp.getProce(),
                "disp" : comp.getDisp(),
            }})
            datos = {}
            continue
        dato = text.split(":")
        datos.update({dato[0] : dato[1]})



