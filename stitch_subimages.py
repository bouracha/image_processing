from image import *

image = IMAGE_OF_CARDS()

image.add_all_cards(stride=256, sub_images_directory='sub_sections/', file_ending='.png')  #file_ending=synthesized_image.jpg

image.write_to_file('test_stitch.jpg')