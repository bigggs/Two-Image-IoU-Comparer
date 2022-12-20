from numpy import asarray
import numpy 
from PIL import Image
import cv2
import csv




count = 1

while 1:
    GT, Generated = [Image.open(x) for x in ['folder1/image'+str(count)+'.png', 'folder2/image'+str(count)+'.png']]




    Background = GT
    Foreground = Generated

    # Vectorise and colourise foreground
    Foreground = Foreground.convert("RGBA")

    pixdata = Foreground.load()
    width, height = Foreground.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] > (240, 240, 240, 240):
                pixdata[x, y] = (255, 255, 255, 0)
            else: 
                pixdata[x,y] = (255,0,0)
    #Foreground.show()
    Foreground = Foreground.convert("RGB")
    #Place foreground ontop of background
    finalImage = Image.blend(Foreground,Background, 0.7)

    finalImage = finalImage.save("IoU/image"+str(count)+".png")
    print('Saved image:' +str(count), end='\r')

    count = count + 1

#Foreground.show()