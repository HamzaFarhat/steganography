import cv2
from PIL import Image
import numpy as np
from cryptography.fernet import Fernet

#Initialize empty string
secretMessageBinary = ""

def decode():
    #Open image to decode and create RGB array
    toDecodeImage = "encoded.png"
    image = cv2.imread(toDecodeImage)

    #Convert rgb image into binary array
    data = np.array(image)
    binaryImage = np.vectorize(np.binary_repr)(data, width=8)

    #Use vectorization method to iterate over each element and retrieve last bit
    #append the bit into the string
    def f(x):
        global secretMessageBinary
        secretMessageBinary += x[-1]
        return x

    vfunc = np.vectorize(f, otypes=[str])
    vfunc(binaryImage)
    
    #Loop over the bit string and convert each byte to ascii character
    decoded = ""
    i = 0
    while i < (len(secretMessageBinary)):
        x = secretMessageBinary[i:i+8]
        y = chr(int(x,2))
        # print(y)
        decoded +=y
        i=i+8
        

    #Cut the decoded message at the delimiter
    finalString = decoded.split("*&")[0]

    #Read encryption key from file
    file = open('key.key', 'rb')
    key = file.read()
    file.close()

    #Use key to decrypt message
    fernet = Fernet(key)
    decrypted = fernet.decrypt(bytes(finalString, 'utf-8'))
    print("Secret message is:", decrypted.decode("utf-8"))

    
    
