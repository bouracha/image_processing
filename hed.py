
import os
from image import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--read_dir', type=str, default='targets/', help='path to data')
parser.add_argument('--write_dir', type=str, default='hed/', help='path to write augmentations')

opt = parser.parse_args()

def apply_hed(path_to_images, path_to_write):
  image_list = os.listdir(path_to_images)
  num_images = len(image_list)

  counter = 0
  for i in image_list:
    counter += 1
    image = IMAGE(path_to_image=path_to_images, name_of_image=str(i))
    if image.valid_image == False:
      continue
    command = 'python pytorch-hed/run.py --model bsds500 --in '+str(path_to_images)+str(i)+' --out '+str(path_to_write)+str(i)
    print(command+' {} processed of {}'.format(counter, num_images))
    os.system(command)
    
 apply_hed(opt.read_dir, opt.write_dir)
