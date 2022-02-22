from numpy import *
from time import sleep

def print_message(f, sense, message, color):
    """A function to print a message on the HAT and in the experiment result file"""
    f.write(message  + "\n")
    for char in message:
      sense.show_letter(char, color)
      sleep(1)
      
def sum(x,y):
    return x+y 

def experiment_formula(f,sense):
    """A function that contains computations with big numbers """
    red = (255, 0, 0)
    x1 = pow(1254.968844, 36)
    x2 = pow(1334.38829, 80)
    x3 = pow(293.1129, 93)
    x4 = pow(8239.1292, 13)
    x5 = pow(932.92928, 47)
    #x6=pow(47487577,464)
    result1=-1.3065339497381586e+199
    result2=2.717995320972408e+229
    r1=double(x1)-double(x2)/double(x4)
    errors=0
    if r1!=result1:
        print_message(f,sense,"Error result 1", red)
        print("error")
        errors=errors+1
    r2=double(x1)-double(x5)+double(x3)
    if r2!=result2 :
        print_message(f,sense,"Error result 2", red)
        errors=errors+1
    r3=double(x4)-double(x3)/double(x1)
    result3=-7.646500423678361e+117
    #result3=-7.6
    if r3!=result3 :
        print_message(f,sense,"Error result 3", red)
        errors=errors+1
    r4=double(x2)-double(x3)+double(x5)
    result4=1.0533622998366155e+250
    if r4!=result4 :
        print_message(f,sense,"Error result 4", red)
        errors=errors+1
    return errors