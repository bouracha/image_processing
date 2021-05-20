from image import *

image1 = IMAGE("../../Desktop/", "parc.png", gray=False)
image2 = IMAGE("../../Desktop/", "heightmap.png", gray=False)
image3 = IMAGE("../../Desktop/", "heightmap_inverted.png", gray=False)

print(image1.shape())
print(image2.shape())
print(image3.shape())

image1.save_section(0, 288, '../../Desktop/', n_H=8800, n_W=13508, save_name='parc_cropped')
image2.save_section(0, 288, '../../Desktop/', n_H=8800, n_W=13508, save_name='heightmap_cropped')
image3.save_section(0, 288, '../../Desktop/', n_H=8800, n_W=13508, save_name='inv_heightmap_cropped')
