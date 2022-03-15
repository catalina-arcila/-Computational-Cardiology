import zipfile
from DICOMtoNIFTI import DICOMtoNIFTI
from threeDtofourD import funcion
from reorient import reoriented
import os
from glob import glob
import dicom2nifti
import numpy as np
#os.mkdir("results")
lista = [7]
for i in lista:
    #ruta_zip = "v"+str(i)+".zip"
    #ruta_extraccion ="v"+str(i)
    #password = None
    #archivo_zip = zipfile.ZipFile(ruta_zip, "r")
    #try:
    #    print(archivo_zip.namelist())
    #    archivo_zip.extractall(pwd=password, path=ruta_extraccion)
    #except:
    #    pass
    #archivo_zip.close()
    DICOMtoNIFTI(i)
    #reoriented(i)
    funcion(i)
    

