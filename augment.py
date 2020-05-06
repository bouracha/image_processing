from image import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--data_dir', type=str, default='targets/', help='path to data')
parser.add_argument('--write_dir', type=str, default='sub_sections/', help='path to write augmentations')
parser.add_argument('--required_height', type=int, default=1656, help='height in pixels desired')
parser.add_argument('--required_width', type=int, default=1024, help='width in pixels desired')
parser.add_argument('--num_images', type=int, default=1, help='number of images in directory (default 1)')
parser.add_argument('--extension', type=str, default='.png', help='extension of files in folder to be read')

opt = parser.parse_args()

for i in range(1, opt.num_images+1):
    print("Augmenting image: {} of {}".format(i, opt.num_images))
    image = IMAGE(path_to_image=opt.data_dir, name_of_image=str(i), extension=opt.extension)
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)
    image.fliplr()
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)

    image = IMAGE(path_to_image=opt.data_dir, name_of_image=i, extension=opt.extension)
    image.flipud()
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)
    image.fliplr()
    image.save_left_centre_right(opt.write_dir, n_H_expected=opt.required_height, n_W_expected=opt.required_width)

    #Finally one warped image is saved
    image = IMAGE(path_to_image=opt.data_dir, name_of_image=str(i), extension=opt.extension)
    image.re_size(n_H_new=opt.required_height, n_W_new=opt.required_width)
    print(opt.write_dir+str(image.name)+'_warped.png')
    image.write_to_file(opt.write_dir+'/'+str(image.name)+'_warped.png')
    image.fliplr()
    image.write_to_file(opt.write_dir+'/'+str(image.name) + '_warped.png')
    image.flipud()
    image.write_to_file(opt.write_dir+'/'+str(image.name)+'_warped.png')
    image.fliplr()
    image.write_to_file(opt.write_dir+'/'+str(image.name) + '_warped.png')