def dress_type(indices, res_points,mask_imgg ):
    
    dress_length = indices[0].max() -  res_points[8][1]

    if  res_points[10] == None:
        leg_length = res_points[13][1] - res_points[11][1]
    else:
        leg_length = res_points[10][1] - res_points[8][1]

    c_copy = mask_imgg.copy()

    cop_res_points = res_points.copy()  
    ratio = dress_length/leg_length
    predict = []

    if   ((ratio >= X[y == 9].min()) and (ratio <= X[y == 9].max())):
            predict.append(9)
    elif ((ratio >= X[y == 8].min()) and (ratio <= X[y == 8].max())):
            predict.append(8)
    elif ((ratio >= X[y == 7].min()) and (ratio <= X[y == 7].max())):
            predict.append(7)
    elif ((ratio > X[y == 6].min()) and (ratio <= X[y == 6].max())):
            predict.append(6)
    elif((ratio > X[y == 5].min()) and (ratio <= X[y == 5].max())):
            predict.append(5)
    elif ((ratio > X[y == 4].min()) and (ratio <= X[y == 4].max())):
            predict.append(4)
    elif ((ratio > X[y == 3].min()) and (ratio <= X[y == 3].max())):
            predict.append(3)
    elif ((ratio > X[y == 2].min()) and (ratio <= X[y == 2].max())):
            predict.append(2)  
    elif ((ratio > X[y == 1].min()) and (ratio <= X[y == 1].max())):
            predict.append(1)
    elif ((ratio > X[y == 0].min()) and (ratio <= X[y == 0].max())):
            predict.append(0)


    return predict
