from image import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--data_dir', type=str, default='targets/', help='path to data')
parser.add_argument('--write_dir', type=str, default='sub_sections/', help='path to write augmentations')
parser.add_argument('--required_height', type=int, default=1536, help='height in pixels desired')
parser.add_argument('--required_width', type=int, default=1024, help='width in pixels desired')

opt = parser.parse_args()

image_list = os.listdir(opt.data_dir)
num_images = len(image_list)

counter = 0
for i in image_list:
    counter += 1
    print("Augmenting image: {} of {}".format(counter, num_images))
    image = IMAGE(path_to_image=opt.data_dir, name_of_image=str(i))
    if image.valid_image == False:
        continue
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)
    image.fliplr()
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)

    image = IMAGE(path_to_image=opt.data_dir, name_of_image=i)
    image.flipud()
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)
    image.fliplr()
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)

    #Finally one warped image is saved
    image = IMAGE(path_to_image=opt.data_dir, name_of_image=str(i))
    image.re_size(n_H_new=opt.required_height, n_W_new=opt.required_width)
    image.write_to_file(opt.write_dir+'/'+str(image.name)+'_warped.png')
    image.fliplr()
    image.write_to_file(opt.write_dir+'/'+str(image.name) + '_warped.png')
    image.flipud()
    image.write_to_file(opt.write_dir+'/'+str(image.name)+'_warped.png')
    image.fliplr()
    image.write_to_file(opt.write_dir+'/'+str(image.name) + '_warped.png')