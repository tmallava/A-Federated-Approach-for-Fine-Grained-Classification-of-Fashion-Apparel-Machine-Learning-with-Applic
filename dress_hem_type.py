def hem_type(image_mask, bound_box, res_points):
 
    if (image_mask[bound_box[3][1]-10, (int((bound_box[3][0] + bound_box[2][0])/2))][2]== 85 and image_mask[bound_box[3][1]-10, (int((bound_box[3][0] + bound_box[2][0])/2))][1]== 0 ):
        
        if  (image_mask[(bound_box[2][1]-10,res_points[8][0]+10)][2] != 85 or image_mask[bound_box[3][1]-10,res_points[11][0]+10][2] != 85): 
             print("Type of Hem: Asymmetrical")
        elif ((bound_box[3][0] - bound_box[2][0]) >= 110):
            print("Type of Hem: Aline")
        else:
            print("type of Hem: straight")
    
    else:
           print("Type of Hem: High low") 
    return