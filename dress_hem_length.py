def dress_type(indices, res_points,mask_imgg ):
    
    dress_length = indices[0].max() -  res_points[8][1]

    if  res_points[10] == None:
        leg_length = res_points[13][1] - res_points[11][1]
    else:
        leg_length = res_points[10][1] - res_points[8][1]

    c_copy = mask_imgg.copy()

    cop_res_points = res_points.copy()  
    Ratio = dress_length/leg_length

    if Ratio <= 0.3:
        print("Type of Dress: Micro Dress")
    if Ratio > 0.3 and Ratio < 0.375:
        print("Type of Dress: Mini Dress")
    if Ratio >= 0.375 and Ratio < 0.45:
        print("Type of Dress: Above knee Dress")
    if Ratio >= 0.45 and Ratio < 0.55:
        print("Type of Dress:  knee Dress")
    if Ratio >= 0.55 and Ratio < 0.65:
        print("Type of Dress: Below knee Dress")
    if Ratio  >= 0.65 and Ratio < 0.7:
        print("Type of Dress: Mid-calf Dress") 
    if Ratio  >= 0.7 and Ratio < 0.75:
        print("Type of Dress: Below Mid-calf Dress") 
    if Ratio  >= 0.75 and Ratio < 0.9:
        print("Type of Dress: Lowercalf Dress")
    if Ratio >= 0.9 and Ratio < 1.05:
        print("Type of Dress: Evening Dress")   
    if Ratio >= 1.05:
        print("Type of Dress: Floor length Dress")

    return
