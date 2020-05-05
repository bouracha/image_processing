### Image Processing


- To download appropriate model to run HED:
```bash
bash setup.sh
```
the rest of the functions can be run from root directory.

- All functions are implemented in an object oriented way in image.py (except for HED which may be called using the apply_hed function in image.py)
```python
from image import *
```

- We can apply HED by providing the (read_directory, write_directory, file_name) in the following way:
```python
image = IMAGE(path_to_image='pytorch-hed/', name_of_image='test_hed', extension='.jpg', gray=False)

```
- Example of object oriented image transformation pipeline (see class for argument changes from default):
```python
image = IMAGE('test_hed.png', gray=True)
image.add_gaussian_noise(mean=0, std=1, scale=100)
image.add_gaussian_blur(kernel_size=(5,5))
```

finally write to file with:
```python
image.write_to_file('final_image.png')
```
# Superresolution: Decomposing and Stitching

For the purpose of stitiching together superresolutions a couple of extra functions were added to the IMAGE class. This requires methods of resizing a the image and iteratively saving segments to it. This can be alled in a loop as implemented in 
```dockerfile
python run_decomposition.py
```
Before running this, however, a folder named 'sub_sections/' must be created to save the produced sub sections. They will automatically be save in the format:
```python
'_'+str(i_H)+'_'+str(i_W)+'_'+str(n_H)+'_'+str(n_W)+'_'+'.png'
```
where (i_H, i_W) is (y,x) position of the top left pixel of the segment and (n_H, n_W) are the sizes of the sub images. This format is used to stitch back together also.
An additional class 
```python
IMAGE_OF_CARDS(object)
```
Is used to stitch all these back together. Usage is as in 
```python
python stich_subimages.py
```
and requires providing the directory name and end of file names in the directory. Also the stride, and dimensionality if differs from default.

# Augmentation pipeline

Pipeline currently implemented you must provide the desired height and width in pixels (this will be the dimensionality of the train and inference images). Now, for each image in the dataset:
- First fits the most dissimilar dimension to the size of the desired corresponding dimension (such that the other dimension is large than required) and then selects 3 subsections:
-- the top/left; centre; and bottom/right along the other dimension. Each are saved to supplied write directory.
- The original image is left-right flipped (mirrored) and the first step is repeated.
- The original image is then up-down flipped and the first step is repeated.
- The original image is then left-right flipped and up-down flipped (flip-flopped one might say) and the first step is repeated.
- Finally the original image is simply warped into the desired dimensions and finally also save.

13 pieces for each image are therefore saved in the current pipeline.

This may all be run with the single commandline:
```commandline
python augment.py --data_dir 'targets/' --write_dir 'sub_sections' --required_height 1656 --required_width 1024 --num_images 2 
```
