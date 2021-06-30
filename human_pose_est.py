import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os
import numpy
import numpy as np
import pandas as pd 
class general_pose_model(object):
    
    def __init__(self):
        #   Body25: 25 points
        #   COCO:   18 points
        #   MPI:    15 points
        self.inWidth = 320
        self.inHeight = 320
        self.threshold = 0.01
        self.pose_net = self.general_coco_model()


    def general_coco_model(self):
            self.points_name = {
                "Nose": 0, "Neck": 1, 
                "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                "LShoulder": 5, "LElbow": 6, "LWrist": 7, 
                "RHip": 8, "RKnee": 9, "RAnkle": 10, 
                "LHip": 11, "LKnee": 12, "LAnkle": 13, 
                "REye": 14, "LEye": 15, 
                "REar": 16, "LEar": 17, 
                "Background": 18}
            self.num_points = 18
            self.point_pairs = [[1, 0], [1, 2], [1, 5], 
                                [2, 3], [3, 4], [5, 6], 
                                [6, 7], [1, 8], [8, 9],
                                [9, 10], [1, 11], [11, 12], 
                                [12, 13], [0, 14], [0, 15], 
                                [14, 16], [15, 17]]
            prototxt = "C:/Users/tmallava/Desktop/Oracle Project/Sprint4/pose/coco/pose_deploy_linevec.prototxt"
            caffemodel = "C:/Users/tmallava/Desktop/Oracle Project/Sprint4/pose/coco/pose_iter_440000.caffemodel"
            coco_model = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)
            return coco_model

    
    def random_choice(self, image_size):
        height, width = image_size
        crop_height, crop_width = 320, 320
        x = random.randint(0, max(0, width - crop_width))
        y = random.randint(0, max(0, height - crop_height))
        return x, y
    
    def safe_resize(self, mat):
        crop_height, crop_width = 320, 320

        ret = cv2.resize(mat, (crop_height, crop_width), interpolation = cv2.INTER_AREA)

        return ret

    def predict(self, imgfile):
        img_cv2 = cv2.imread(imgfile)
        img_height, img_width, _ = img_cv2.shape
        inpBlob = cv2.dnn.blobFromImage(img_cv2, 
                                        1.0/ 255,    #
                                        (self.inWidth, self.inHeight),
                                        (104, 117, 123), 
                                        swapRB=False, 
                                        crop=False)
        self.pose_net.setInput(inpBlob)
        self.pose_net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.pose_net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)

        output = self.pose_net.forward()
        
        H = output.shape[2]
        W = output.shape[3]

        points = []
        for idx in range(self.num_points):
            probMap = output[0, idx, :, :] # confidence map.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
            x = (img_width * point[0]) / W
            y = (img_height * point[1]) / H
            if prob > self.threshold:
                points.append((int(x), int(y)))
            else:
                points.append(None)

        return points


    def vis_pose(self, imgfile, points):
        img_cv2 = cv2.imread(imgfile)
        img_cv2_copy = np.copy(img_cv2)
        img_height, img_width, _ = img_cv2.shape
        scale = 1
        fontScale = min(img_width,img_height)/(700/scale)
        for idx in range(len(points)):
            if points[idx]:
                cv2.circle(img_cv2_copy, 
                           points[idx], 
                           2, 
                           (0, 255, 255), 
                           thickness=-1,
                           lineType=cv2.FILLED)
                cv2.putText(img_cv2_copy, 
                            "{}".format(idx), 
                            points[idx], 
                            cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale, 
                            (0, 0, 255), 
                            1, 
                            cv2.LINE_AA , False)
                
        #cv2.rectangle(img_cv2_copy,(indices[1].min(),indices[0].min()),(indices[1].max(),indices[0].max()),(0,255,0),3)

        #for i in bound_box: 
            #cv2.circle(img_cv2_copy, i,2, (255, 0, 0), 
                           #thickness=-1,
                           #lineType=cv2.FILLED)

        #cv2.imwrite('C:/Users/tmallava/Downloads/Image_pairs/above_knee_dress.png', img_cv2_copy)
        for pair in self.point_pairs:
            partA = pair[0]

            partB = pair[1]

            if points[partA] and points[partB]:
                cv2.line(img_cv2, 
                         points[partA], 
                         points[partB], 
                         (0, 255, 255), 2)
                cv2.circle(img_cv2, 
                           points[partA], 
                           2, 
                           (0, 0, 255), 
                           thickness=-2)# lineType=cv2.FILLED)
                           

        plt.figure(figsize=[10, 10])
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(img_cv2_copy, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.show()

        return img_cv2
