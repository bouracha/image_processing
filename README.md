### Image Processing


-To download appropriate model to run HED:
```bash
bash setup.sh
```
the rest of the functions can be run from root directory.

-Example of python functions currently implemented:
```python
from image import *
apply_hed("pytorch-hed/", '', 'test_hed')
image = IMAGE('test_hed.png')
image.add_gaussian_noise()
image.add_gaussian_blur()
```
- finally write to file with:
```python
image.write_to_file('final_image.png')
```
