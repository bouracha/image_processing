from image import *

image = IMAGE_OF_CARDS()


image.add_all_cards(stride=256)

image.write_to_file('test_stitch.jpg')