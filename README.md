### Image Processing


- To download appropriate model to run HED:
```bash
bash setup.sh
```
the rest of the functions can be run from root directory.

All functions are implemented in an object oriented way in image.py (except for HED which may be called using the apply_hed function in image.py)
```python
from image import *
```

- Example of python functions currently implemented:
```python
apply_hed("pytorch-hed/", '', 'test_hed')
image = IMAGE('test_hed.png')
image.add_gaussian_noise()
image.add_gaussian_blur()
```
finally write to file with:
```python
image.write_to_file('final_image.png')
```
