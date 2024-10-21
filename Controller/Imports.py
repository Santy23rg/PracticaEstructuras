from pathlib import Path
import sys

# Obtener la ruta del directorio actual
current_dir = Path(__file__).parent

# Construir la ruta relativa
model_path = current_dir / '../Model'
controller_path = current_dir / '../Controller'

# Importar el módulo
sys.path.append(str(model_path))

from EstudianteDis import EstudianteDis
from Tablet import *
from BD import *
