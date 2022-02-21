from computations import sum
from computations import experiment_formula
from sense_hat import SenseHat
from sense_emu import SenseHat
from time import sleep
import time
from pathlib import Path


def print_message(f,message,color):
    f.write(message  + "\n")
    sense.clear()
    for char in message:
      sense.show_letter(char, color)
      sleep(1)
      
base_folder = Path(__file__).parent.resolve()      
f = open(base_folder + "/experiment_result.txt", "w")    
sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

print_message("Starting experiment",blue)
start_time = time.time()
seconds = 4
f.write("Starting time: " + str(time.ctime(start_time)) + "\n")
humidity=0
while True:
    errors=experiment_formula()
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= seconds:
        break
    if humidity != 0;
        humidity = round(sense.humidity,4)
        print_message("Humidity"+str(humidity))
    
if errors > 0:
    print_message("Found"+str(errors) +" errors",red)
    f.write("Found"+str(errors) +" errors")
    print("Found errors")
else:
    print_message("No errors",green)
    f.write("No errors")
    print("No errors")
f.write("Ending time: " + str(time.ctime(start_time)) + "\n")
f.close()
print_message("Experiment completed",green)
