from nibabel.nifti1 import save
from nilearn import image
#smoothed_img = image.smooth_img('/home/user/t_map001.nii')  
# Example with a smoothing process:
from nilearn.image import smooth_img, concat_imgs, mean_img
from nilearn.image.image import iter_img, load_img
#result_img = smooth_img("nifti/time_*.nii.gz") 
result_img = load_img("nifti/time_*.nii.gz") 
print(result_img)
print(type(result_img))
#fmri_img = concat_imgs(result_img)
#mean_img = mean_img(fmri_img)
#i = iter_img(fmri_img)
save(result_img,"prueba 1")
print('ggg')