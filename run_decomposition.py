from image import *

image = IMAGE("../../Desktop/best_so_far.jpg", gray=False)
print(image.shape())

image.re_size()
print(image.shape())

image.decompose_image(stride=256)
