from computations import sum
from computations import experiment_formula
#from sense_hat import SenseHat
from time import sleep
import time

#sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

#sense.show_letter("S", red)
#sleep(1)
#sense.show_letter("t", blue)
#sleep(1)
#sense.show_letter("a", green)
#sleep(1)
#sense.show_letter("r", white)
#sleep(1)
#sense.show_letter("t", yellow)
#sleep(1)
#sense.show_letter("i", red)
#sleep(1)
#sense.show_letter("n", red)
#sleep(1)
#sense.show_letter("g", red)
#sleep(1)
#d=sum(1,2)
#print(d)



start_time = time.time()
seconds = 4
f = open("experiment_result.txt", "w")
f.write("Starting time: " + str(time.ctime(start_time)) + "\n")
while True:
    experiment_formula()
    current_time = time.time()
    elapsed_time = current_time - start_time
    f.write("Elapsed time: " + str(elapsed_time) + "\n")
    if elapsed_time >= seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break
f.close()

