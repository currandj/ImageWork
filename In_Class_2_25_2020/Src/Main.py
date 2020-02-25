'''
Created on Feb 25, 2020

@author: currandj
'''
from image_functions import *

# open an image file. The default path is where this python module is
im = Image.open("SiriusAndViolet.jpg")
print(im.width, im.height, im.mode, im.format)  # Display some info about the image
'''
my_image = load_image("XSiriusAndViolet.jpg")
my_image.show(my_image)
'''
#Make use of crop_image
#1. Load Image, 2. Call crop Image and save what it returns, 3. Call show to display results

im = Image.open("SiriusAndViolet.jpg")
im_cropped = crop_image(im, (200,300,400,500))
im_cropped.show()