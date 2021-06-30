def sleeve_length(res_points,image_mask ):
    if (image_mask[res_points[5][1],res_points[5][0]][2]== 85 or image_mask[res_points[2][1],res_points[2][0]][2]== 85):
        if (image_mask[int((res_points[5][1]  + res_points[6][1])/2-5),int((res_points[5][0]  + res_points[6][0])/2-5)][2]== 85 and image_mask[int((res_points[2][1]  + res_points[3][1])/2-5),int((res_points[2][0]  + res_points[3][0])/2-5)][2]== 85):
            if (image_mask[res_points[6][1]-5,res_points[6][0]][2]!= 85 and image_mask[res_points[3][1]-5,res_points[3][0]][2]!= 85):
                print("Type of sleeves: short sleeves")
                
            elif (image_mask[res_points[7][1],res_points[7][0]][2]!= 85 and image_mask[res_points[4][1],res_points[4][0]][2]!= 85):
                if (image_mask[int((res_points[7][1]  + res_points[6][1])/2-10 ),int((res_points[7][0]  + res_points[6][0])/2-10)][2]== 85 and image_mask[int((res_points[4][1]  + res_points[3][1])/2-10 ),int((res_points[4][0]  + res_points[3][0])/2-10)][2]== 85): 
                    print("Type of sleeves: bracelet sleeves")
                else:
                    print("Type of sleeves: Elbow sleeves")
            else:
                print("Type of sleeves: Long sleeves")
        else: 
                print("Type of sleeves: cap sleeves")
    else:
        print("Type of sleeves: No sleeves")


    return