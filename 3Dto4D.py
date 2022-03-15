from nibabel.nifti1 import save
from nilearn.image.image import load_img


def funcion(i):
    #result_img = load_img("nifti_v"+str(i)+"_reoriented/time_*.nii.gz") 
    result_img = load_img("nifti_v"+str(i)+"/time_*.nii.gz") 

    print(result_img.shape)
    #print(type(result_img))
    save(result_img,"results_v2/v"+str(i)+".nii.gz")