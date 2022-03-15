import os
from glob import glob
import dicom2nifti

def DICOMtoNIFTI(j):
    path_time_folders = "v"+str(j)+"/v"+str(j)+"/cSAX/*"
    path_outcomes = "nifti_v"+str(j)
    os.mkdir(path_outcomes)
    for i, time in enumerate(glob(path_time_folders)):
        dicom2nifti.dicom_series_to_nifti(time, os.path.join(path_outcomes,"time_"+str(i+1)+".nii.gz"), reorient_nifti=False)