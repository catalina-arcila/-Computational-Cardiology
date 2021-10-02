import os
from glob import glob
import dicom2nifti

path_time_folders = "v1/v1/cSAX/*"
path_outcomes = "nifti"

for i, time in enumerate(glob(path_time_folders)):
    dicom2nifti.dicom_series_to_nifti(time, os.path.join(path_outcomes,"time_"+str(i+1)+".nii.gz"))