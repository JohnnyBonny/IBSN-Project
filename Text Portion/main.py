import cv2
import pytesseract
import numpy as np
#print("Package imported")

#to call pytesseract libaray
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\13106\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
"""
img = cv2.imread("download.png") #get image
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to RBG
cong = r' --oem 3 --psm 6 outputbase digits' # to only include numbers

# to shapen an image
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)


hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
"""
#to instantiate which file to use
image = cv2.imread('isbn.png')

# to shapen an image so that the letters and words can be easily identifiable
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

#greyscale the image so that we can pass it into the adaptiveThreshold function
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#we use adaptive threshold to convert the image into make it easier to identify the letters in differnt lighting situations
#via the ADAPTIVE_THRESH_GAUSSIAN_C. The THRESH_BINARY converts the image into a binary image
image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

if __name__ == '__main__':

    print(pytesseract.image_to_string(image))
    #print(pytesseract.image_to_data(image))

    cv2.imshow("Output",image)
    #cv2.waitKey(0)
    """
    cv2.imshow('AV CV- Winter Wonder Sharpened', image_sharp)
    """
    cv2.waitKey(0)

