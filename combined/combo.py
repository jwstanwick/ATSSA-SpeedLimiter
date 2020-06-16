from imutils import build_montages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
from os import path
import time
import sys
from skimage import io

def image_colorfulness(image):
	(B, G, R) = cv2.split(image.astype("float"))
	rg = np.absolute(R - G)
	yb = np.absolute(0.5 * (R + G) - B)
	(rbMean, rbStd) = (np.mean(rg), np.std(rg))
	(ybMean, ybStd) = (np.mean(yb), np.std(yb))
	stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
	meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2))
	return stdRoot + (0.3 * meanRoot)

while 1==1:
	if path.exists('input.jpg'):
		image = cv2.imread('input.jpg')
		image = imutils.resize(image, width=250)
		C = image_colorfulness(image)

		if C > 50:
			C = 50
		C = C/50

		print('colorfulness ' + str(C))

		inputImage = 'input.jpg'

		img = cv2.imread(inputImage,0)
		cv2.imwrite('output.jpg',img)
		image = io.imread('output.jpg')
		
		if np.mean(image) > 100:
			lightVal = 1
		else:
			lightVal = np.mean(image)/100

		print('light ' + str(lightVal))

		combo = str(lightVal*0.2+C*0.8)
		print('combined ' + combo)

		original_stdout = sys.stdout

		with open('output.txt', 'w') as f:
			sys.stdout = f
			print(combo)
			sys.stdout = original_stdout
		print(" ")
	else:
		print('no image')
	time.sleep(1)