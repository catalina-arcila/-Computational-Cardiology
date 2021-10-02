# Computational-Cardiology

Dado un conjunto de datos DICOM Series(conjunto de DICOM Single Image en una misma carpeta) se convierte a nifti 3D mediante el archivo `DICOMtoNIFTI.py`. Para el funcionamiento de este archivo de debe tener en una carpeta(`path_time_folders`) las carpetas de los distintos tiempos que posee los datos de las imágenes de la resonancia magnética cardíaca. Se cargan los archivos de cada tiempo y se convierte en NIFTI 3D y se guarda en una carpeta (`path_outcomes`).

Posteriormente, se usa el archito `3Dto4D.py` que lo que hace es juntar todos los archivos NIFTY 3D del tiempo y crea un archivo NIFTI 4D (3D + tiempo).
