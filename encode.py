import cv2
from PIL import Image
import numpy as np
counter = 0
import sys
def spaceChecker(image, message):
  width, height = image.shape[0], image.shape[1]
  placesToStore = width * height * 3
  numberOfDigitsToEncode = len(message) * 8
  
  if placesToStore >= numberOfDigitsToEncode:
    return True
  else:
    return False   


def encode():
    #Get the secret message from user
    secret = input("Enter your secret message:\n")

    #Open image file and resize it to a manageable size
    img = "input.jpg"
    image = cv2.imread(img)
    resize = cv2.resize(image, (50, 50))

    #Convert image into binary array
    data = np.array(resize)
    binaryImage = np.vectorize(np.binary_repr)(data, width=8)

    #Convert secret to binary
    delim = "*&"
    s=secret+delim
    updatedSecret = ''.join('{0:08b}'.format(ord(x), 'b') for x in s)

    #Check if image pixel size is large enough to hold the secret
    if not spaceChecker(resize, updatedSecret):
        exit("Image too small")

    #Use vectorization method to take the first 7 digits of the image byte and concatenate
    #each bit of the secret message then convert it into decimal RGB value
    def f(x):
        global counter
        if counter < len(updatedSecret)-1:
            binaryElements = x[:7]
            str = binaryElements + updatedSecret[counter]
            number = int(str, 2)
            counter +=1
            return number
        else:
            number = int(x, 2)
            return number

    vfunc = np.vectorize(f, otypes=[int])
    alteredData = vfunc(binaryImage)

    #Write new image file
    cv2.imwrite("encoded.png", alteredData)

    #Closing
    print("Encoding completed, check encoded.jpg!")
    