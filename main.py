from logzero import logger, logfile
from time import sleep
import time
from pathlib import Path
from sense_hat import SenseHat
from datetime import datetime, timedelta
import csv

def print_message(f, sense, message, color):
    """A function to print a message on the HAT and in the experiment result file"""
    f.write(message  + "\n")
    logger.info(message)
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
    result1=-1.3065339497381586e+199
    result2=2.717995320972408e+229
    r1=x1-x2/x4
    errors=0
    if r1!=result1:
        print_message(f,sense,"Error result 1", red)
        logger.info("error result 1")
        logger.info("error")
        errors=errors+1
    r2=x1-x5+x3
    if r2!=result2 :
        print_message(f,sense,"Error result 2", red)
        logger.info("error result 2")
        logger.info("error")
        errors=errors+1
    r3=x4-x3/x1
    result3=-7.646500423678361e+117
    if r3!=result3 :
        print_message(f,sense,"Error result 3", red)
        logger.info("error result 3")
        logger.info("error")
        errors=errors+1
    r4=x2-x3+x5
    result4=1.0533622998366155e+250
    if r4!=result4 :
        print_message(f,sense,"Error result 4", red)
        logger.info("error result 4")
        logger.info("error")
        errors=errors+1
    return errors

def create_csv(data_file):
    """A function to create a csv file"""
    logger.info("creating csv file")
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Humidity value", "Number of errors")
        writer.writerow(header)
        
def add_csv_data(data_file, data):
    """A function to add data into the csv file"""
    logger.info("adding data to csv file")
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
base_folder = Path(__file__).parent.resolve()      
f = open(f"{base_folder}/experiment_result.txt", "w")
data_file = base_folder/'data.csv'
create_csv(data_file)
logfile(base_folder/"events.log")

sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

print_message(f,sense,"Starting experiment",blue)
logger.info("Starting experiment")

"""Create a `datetime` variable to store the start time"""
start_time = datetime.now()
"""Create a `datetime` variable to store the current time"""
"""(these will be almost the same at the start)"""
now_time = datetime.now()
"""Run a loop for 170 minutes (10 minutes earlier to be sure we are on time)"""
running_time = 170

logger.info("Starting time: " + str(now_time) + "\n")

while (now_time < start_time + timedelta(minutes=running_time)):
    try: 
        errors=experiment_formula(f, sense)
        current_time = time.time()
        """ Reading humidity """
        humidity = round(sense.humidity,2)
        print_message(f,sense,"Humidity "+str(humidity), yellow)
        logger.info("Humidity "+str(humidity))
        row = (datetime.now(),humidity, errors)
        add_csv_data(data_file, row)
        """Update the current time"""
        now_time = datetime.now() 
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
"""Display errors (if any)"""        
if errors > 0:
    print_message(f,sense,"Found "+str(errors) +" error(s)",red)
else:
    print_message(f,sense, "No errors",green)
logger.info("Ending time: " + str(now_time) + "\n")
print_message(f,sense,"Experiment completed",green)
logger.info("Experiment completed")
"""Close sense hat and the file"""
sense.clear()       
f.close()
logger.info("Sense hat and file closed")
