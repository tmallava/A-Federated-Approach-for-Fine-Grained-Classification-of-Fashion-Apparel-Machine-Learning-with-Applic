import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os
import numpy
import numpy as np
import pandas as pd 


def bounding_box(thresh, image):
    indices = numpy.where(thresh == [25])
    bound_box = [(indices[1].min(),indices[0].min()),  #1    
          (indices[1].max(), indices[0].min()), #2
          (indices[1].min(),indices[0].max()),  #3    
          (indices[1].max(), indices[0].max())] #4


    cv2.rectangle(image,(indices[1].min(),indices[0].min()),(indices[1].max(),indices[0].max()),(0,255,0),1)

    for i in bound_box: 
        cv2.circle(image, i,10, (0, 0, 255), 
                               thickness=-1,
                               lineType=cv2.FILLED)
    
    return bound_box