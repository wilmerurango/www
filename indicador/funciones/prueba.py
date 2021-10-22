import xlrd
import os
# import numpy as np

def importar_datos():
    archi = xlrd.open_workbook(os.path.join("archivo.xlsx"))
    hoja1 = archi.sheet_by_index(0)
    return hoja1
