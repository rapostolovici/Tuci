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
    result1=-1.3065339497381586e+199
    result2=2.717995320972408e+229
    r1=double(x1)-double(x2)/double(x4)
    errors=0
    if r1!=result1:
        print("error")
        errors=errors+1
    r2=double(x1)-double(x5)+double(x3)
    if r2!=result2 :
        print("error")
        errors=errors+1
    print(r1)
    print(r2)
    r3=double(x4)-double(x3)/double(x1)
    print(r3)
    result3=-7.646500423678361e+117
    if r3!=result3 :
        print("error")
        errors=errors+1
    r4=double(x2)-double(x3)+double(x5)
    print(r4)
    result4=1.0533622998366155e+250
    if r4!=result4 :
        print("error")
        errors=errors+1
    return errors
