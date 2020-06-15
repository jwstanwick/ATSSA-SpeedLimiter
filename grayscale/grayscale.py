'''
Prereqs: numpy | matplotlib

This is v1.0 of the robust application
The code below should be able to handle a lot more fine tuning, if needed

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])
    #The line above can be edited in that the ending of the file is in the format of RGB strength (R,G,B)
img = mpimg.imread('image.png')

gray = rgb2gray(img)

plt.imshow(gray, cmap = plt.get_cmap('gray'))

plt.savefig('image_greyscale.png')
plt.show()'''

'''
Prereqs: Pillow (referenced as PIL)
This implementation is much more simple, and not as customizable but gets the job done quite evenly'''

from skimage import io
import cv2
import numpy as np
import sys

inputImage = 'input.jpg'

img = cv2.imread(inputImage,0)
cv2.imwrite('output.jpg',img)
image = io.imread('output.jpg')

np.mean(image)
  
stdout_fileno = sys.stdout
sys.stdout = open('rating.txt', 'w')

for ip in sample_input:
    sys.stdout.write(print(np.mean(image)) + '\n')
  
sys.stdout.close()
sys.stdout = stdout_fileno