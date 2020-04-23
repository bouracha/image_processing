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
apply_hed("pytorch-hed/", '', 'test_hed')
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
