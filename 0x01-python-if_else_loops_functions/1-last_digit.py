#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("Last digit of the number, is {} and is greater than 5".format(number))
elif number == 0:
    print("Last digit of the number, is {} and is 0".format(number))
elif number < 6 and not 0:
    print("Last digit of the number, is {} and is less than 6 and not 0".format(number))
