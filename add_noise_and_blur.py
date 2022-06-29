from image import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--data_dir', type=str, default='targets/', help='path to data')

opt = parser.parse_args()

image_list = os.listdir(opt.data_dir)
num_images = len(image_list)

counter = 0
for i in image_list:
    counter += 1
    print("Adding noise to image: {} of {}: {}".format(counter, num_images, i))
    image = IMAGE(path_to_image=opt.data_dir, name_of_image=str(i))
    if image.valid_image == False:
        continue
    image.add_gaussian_noise()
    image.add_gaussian_blur()
    
    image.write_to_file(opt.data_dir+'/'+str(i))
