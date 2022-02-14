from computations import sum
from computations import experiment_formula
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

sense.show_letter("S", red)
sleep(1)
sense.show_letter("t", blue)
sleep(1)
sense.show_letter("a", green)
sleep(1)
sense.show_letter("r", white)
sleep(1)
sense.show_letter("t", yellow)
sleep(1)
sense.show_letter("i", red)
sleep(1)
sense.show_letter("n", red)
sleep(1)
sense.show_letter("g", red)
sleep(1)
#d=sum(1,2)
#print(d)

experiment_formula()

