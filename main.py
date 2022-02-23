from computations import sum
from computations import experiment_formula,print_message
from logzero import logger, logfile
from time import sleep
import time
from pathlib import Path
from sense_hat import SenseHat

def print_message(f, sense, message, color):
    """A function to print a message on the HAT and in the experiment result file"""
    f.write(message  + "\n")
    for char in message:
      sense.show_letter(char, color)
      sleep(1)

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

base_folder = Path(__file__).parent.resolve()      
f = open(f"{base_folder}/experiment_result.txt", "w")    
sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

logfile(base_folder/"events.log")

print_message(f,sense,"Starting experiment",blue)
start_time = time.time()
seconds = 15
f.write("Starting time: " + str(time.ctime(start_time)) + "\n")
while True:
    try: 
        errors=experiment_formula(f, sense)
        current_time = time.time()
        elapsed_time = current_time - start_time
        """ Read humidity from 5 to 5 seconds """
        if elapsed_time % 5:
            """ Reading humidity """
            humidity = round(sense.humidity,2)
            print_message(f,sense,"Humidity "+str(humidity), yellow)
    
        
        if elapsed_time >= seconds:
            break
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
""" Display errors (if any)"""        
if errors > 0:
    print_message(f,sense,"Found "+str(errors) +" error(s)",red)
else:
    print_message(f,sense, "No errors",green)
f.write("Ending time: " + str(time.ctime(start_time)) + "\n")
print_message(f,sense,"Experiment completed",green)
sense.clear()       
f.close()   
