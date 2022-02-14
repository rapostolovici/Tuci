from numpy import *

def sum(x,y):
    return x+y 

def experiment_formula():
    x1 = pow(1254.968844, 36)
    #print(x1)
    x2 = pow(1334.38829, 80)
    #print(x2)
    x3 = pow(293.1129, 93)
    #print(x3)
    x4 = pow(8239.1292, 13)
    #print(x4)
    x5 = pow(932.92928, 47)
    x6=pow(47487577,464)
    #print(x5)
    r1=double(x1)-double(x2)/double(x4)+double(x6)
    r2=double(x1)-double(x5)+double(x3)
    print(r1)
    print(r2)
    

