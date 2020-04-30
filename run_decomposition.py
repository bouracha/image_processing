from image import *

image = IMAGE("../../Desktop/best_so_far.jpg", gray=False)
image.shape()

image.re_size()
image.shape()

image.decompose_image(stride=64)
