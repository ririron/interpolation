import numpy as np

def lagrange(x, y, input_x):

    #print(type(range(len(x))))
    
    ans = 0
    for index in range(len(x)):
        z = calc_z(x, input_x, index)
        ans += z * y[index]


    return ans

def calc_z(data, input_x, z_num):
    bunbo = 1
    bunshi = 1
    for d in data:
        if d != data[z_num]:
            bunshi *= input_x - d
            bunbo *= data[z_num] - d

    return bunshi/bunbo
