import numpy as np
import cv2
import os
import sys



def apply_hed(path_to_image, path_to_write, name):
  command = 'python pytorch-hed/run.py --model bsds500 --in '+str(path_to_image)+str(name)+'.jpg --out '+str(path_to_write)+str(name)+'.png'
  print(command)
  os.system(command)

class IMAGE(object):

  def __init__(self, path_to_image, gray=True):
    self.gray=gray
    if gray==True:
      self.image = cv2.imread(path_to_image, cv2.COLOR_BGR2GRAY)
      self.n_H, self.n_W = self.image.shape
    else:
      self.image = cv2.imread(path_to_image)
      self.n_H, self.n_W, self.n_C = self.image.shape

  def add_gaussian_noise(self, mean=0, std=1, scale=100):
    if (self.gray==True):
      noise = scale*np.random.rand(self.n_H, self.n_W)
      img_with_noise = self.image + noise
      self.image = img_with_noise
    else:
      noise = scale*np.random.rand(self.n_H, self.n_W, self.n_C)
      img_with_noise = self.image + noise
      self.image = img_with_noise

  def add_gaussian_blur(self, kernel_size=(5,5)):
    image_with_blur = cv2.GaussianBlur(self.image,kernel_size,cv2.BORDER_DEFAULT)
    self.image = image_with_blur
  
  def write_to_file(self, path_to_write):
    cv2.imwrite(path_to_write, self.image)

  def shape(self):
    return(self.image.shape)

  def re_size(self, n_H_new=8192, n_W_new=8192):
    self.image = cv2.resize(self.image, (n_H_new, n_W_new))
    self.n_H, self.n_W = n_H_new, n_W_new

  def save_section(self, i_H, i_W, folder_to_save, n_H=1024, n_W=1024):
    sub_image = self.image[i_H: i_H+n_H, i_W: i_W+n_W]
    cv2.imwrite(str(folder_to_save)+'/'+str(i_H)+'_'+str(i_W)+'_'+str(n_H)+'_'+str(n_W)+'.png', sub_image)

  def decompose_image(self, n_H_sub=1024, n_W_sub=1024, stride=64):
    num_subsections_processed = 0
    num_subsections = ((self.n_H - n_H_sub + 1)/stride)*((self.n_W - n_W_sub + 1)/stride)
    for i_H in range(0, self.n_H - n_H_sub + 1, stride):
      for i_W in range(0, self.n_W - n_W_sub + 1, stride):
        self.save_section(i_H, i_W, 'sub_sections', n_H_sub, n_W_sub)
        num_subsections += 1
        print("Number subsections= "+str(num_subsections_processed)+"/"+str(num_subsections))
    print("Number of subsections: ", num_subsections_processed)



