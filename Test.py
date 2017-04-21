
from imageprocessing import ImageProcessing
from PIL import Image, ImageFilter

processor = ImageProcessing("Glitch.jpg")


imageOut = processor.invert(green = False, blue = False)
imageOut.save("output - invert.jpg")

imageOut = processor.embossFilter()
imageOut.save("output - emboss.jpg")

imageOut = processor.grayScale()
imageOut.save("output - grayscale.jpg")

imageOut = processor.imageGlitch()
imageOut.save("output - Glitch.jpg")

imageOut = processor.imageGlitchTwo()
imageOut.save("output - GlitchTwo.jpg")
