#Fogo Doom sem paleta de cores

import cv2 as cv
import numpy as np
from random import randint
from random import randint
# (mHig - 1) * mWid = 6'400
tPix = 20 #(10)
mHig = tPix*20 #Precisa ser multiplo de pixel mais fTam.(20)
mWid = tPix*20 #Precisa ser multiplo de tPix.(20)
decay = 30 #Inverso da intensidade (30)
add = 5 #Incremento/Decremento pelas teclas 'a' e 'd'
font = 255
matriz = np.zeros((mHig, mWid, 3), np.uint8)

#Iniciação/perpetuação do fogo
while(True):
	for col in range(0, mWid, tPix):
		for lin in range(0, mHig, tPix):
			if lin == mHig - tPix:
				att = font - randint(0, decay)
			else:
				#att = matriz[lin + tPix][col][2] - randint(0, decay)
				att = matriz.item(lin + tPix, col, 2) - randint(0, decay)
			if att > 0:
				for l in range(0,tPix):
					for c in range(0,tPix):
						#matriz[lin + l][col + c][2] = att
						matriz.itemset((lin + l, col + c, 2), att)
	cv.imshow('frame',matriz)
	key = cv.waitKey(1)
	if key & 0xFF == ord('q'):
	    break
	if key == 97:
		decay += add
	if key == 100 and decay > add:
		decay -= add
	if key == 115 and font >= 0:
		font -= 20
	if key == 119 and font < 255:
		font += 20
cv.destroyAllWindows()