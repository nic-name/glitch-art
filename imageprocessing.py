#Image Processing Class with image processing and filtering

import math
import random
from PIL import Image, ImageFilter, ImageTk
from array import *

class ImageProcessing:

    #some intialisers
    def __init__(self, w, h):
        #empty image
        self.width, self.height = w, h
        self.name = "noname.jpg"
        self.image = Image.new("RGB", (self.width, self.height), 0)
    #end init
    #you can make as many initialisers as you like once they contain different args
        
    def __init__(self, name):
        #image loaded from the file name
        self.name = name
        self.image = Image.open(self.name)
        self.width, self.height = self.image.width, self.image.height
    #end init

    #some IP methods
    def invert(self, red = True, green = True, blue = True):
        #open an empty image
        newImage = Image.new("RGB", (self.width, self.height))
        
        #traverse the image to invert (r,g,b)
        for i in range(self.width):
            for j in range(self.height):
                #i,j surrounded by an extra bracket making it a tuple
                r,g,b = self.image.getpixel((i,j))
                if red :
                    newR = 255 -r
                else :
                    newR = r
                #endif

                if green :
                    newG = 255 -g
                else :
                    newG = g
                #endif
                    
                if blue :
                    newB = 255 -b
                else :
                    newB = b
                #endif
                newImage.putpixel((i,j), (newR, newG, newB))
            #endfor
        #endfor
        return newImage
    #end invert

    #some image filtering
    def embossFilter(self):
        #EMBOSS is a predefined filter in the class
        return self.image.filter(ImageFilter.EMBOSS)
            
        #save the new image

    def  grayScale(self):
        #open an empty image
        newImage = Image.new("RGB", (self.width, self.height))
        
        #traverse the image to invert (r,g,b)
        for i in range(self.width):
            for j in range(self.height):
                r,g,b = self.image.getpixel((i,j))
                gray =((r+g+b)//3)
                newImage.putpixel((i,j), (gray, gray, gray))
            #return gray
            #endfor
            
        #endfor
        return newImage
    #end grayscale



    def imageGlitch(self):
        newImage = Image.new("RGB", (self.width, self.height))
        glitch_percent = 10 #percentage of image affectesd

        #traverse the image to invert (r,g,b)
        for i in range(self.width):
            for j in range(self.height):
                #i,j surrounded by an extra bracket making it a tuple
                r,g,b = self.image.getpixel((i,j))
                doGlitch = random.randint(0,100) < glitch_percent
                if doGlitch :
                    newR = 255 -r
                    newG = 255 -g
                    newB = 255 -b

                    
                else :
                    newR = r
                    newG = g
                    newB = b

                #endif
                newImage.putpixel((i,j), (newR, newG, newB))
            #endfor
        #endfor
        return newImage

    #endimageGlitch

    
    def imageGlitchTwo(self, red = True, green = True, blue = True):
        newImage = Image.new("RGB", (self.width, self.height))

        imageFraction = 20 # => 1/20
        swapEveryXblock = 3
        
        area = self.width * self.height
        counter = 0
        imageBlockLength = int(area/imageFraction)
        tempArray = []
        
        for i in range(self.width):
            for j in range(self.height):
                r,g,b = self.image.getpixel((i,j))
                imageBlock = int(counter/imageBlockLength)
                arrayIndex = int(counter % imageBlockLength)
                
                if len(tempArray) <= arrayIndex :
                    tempArray.append([])
                #endIf
                    
                if imageBlock>0 and imageBlock%swapEveryXblock ==0 :
                    newR = tempArray[arrayIndex][0]
                    newG = tempArray[arrayIndex][1]
                    newB = tempArray[arrayIndex][2]

                else :
                    newR = r
                    newG = g
                    newB = b                
                #endif

                tempArray[arrayIndex] = [r, g, b]

                newImage.putpixel((i,j), (newR, newG, newB))
                counter = counter + 1
                #endfor
            #endfor
        print("Complete")
        return newImage
        
    #end glitch

