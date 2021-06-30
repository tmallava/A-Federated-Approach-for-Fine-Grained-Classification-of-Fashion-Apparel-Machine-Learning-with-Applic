from PIL import Image
import cv2
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def conv_gray(img_mask):
    image = img_mask #img_cv
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#image

    m = gray
    h,w = np.shape(gray)
    np.unique(gray) # 0  25  29  40  75  76  79 129 172 179 194 210 226
    for py in range(0,h):
        for px in range(0,w):

            if(gray[py][px] > 25):            
                gray[py][px]=255
            if(gray[py][px] < 25):            
                gray[py][px]=255

    thresh = cv2.threshold(gray,232,255,cv2.THRESH_TRUNC)[1]

    plt.imshow(thresh)
    plt.imshow(img_mask)

    indices = np.where(thresh == [25])
    return thresh, indices
