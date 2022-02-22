from computations import sum
from computations import experiment_formula,print_message
from logzero import logger, logfile
from time import sleep
import time
from pathlib import Path
from sense_hat import SenseHat

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
