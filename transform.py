import numpy as np
import random as rand
def transform_colums():
    array = np.arange(1,51,1, dtype= float).reshape(5,10)
    colmean = np.mean(array, axis=0)
    colmax = np.amax(array, axis = 0)
    for x in range(0,5):   
        for y in range(0,10):
            #print(colmean[y])
            #print(colmax[y])
            array[x, y] = (array[x,y] - colmean[y])/colmax[y]
    print(array)
    return array
transform_colums()