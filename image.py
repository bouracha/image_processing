import numpy as np
import cv2
import os


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
      self.image = cv2.imread(path_to_image, cv2.COLOR_BGR2GRAY)
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



