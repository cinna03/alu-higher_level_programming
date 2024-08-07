#!/usr/bin/python3
import random
<<<<<<< HEAD

number = random.randint(-10000, 10000)
if number >= 0:
    digit = number % 10
else:
    digit = abs(number) % 10 * -1

 print("Last digit of {} is {}".format(number, digit), end=" ")


 if digit > 5:
     print("and is greater than 5")

elif digit == 0:
=======
number = random.randint(-10000, 10000)
if number > 0:
    digit = number % 10
else:
    digit = ((number * -1) % 10) * -1
print("Last digit of {} is {}".format(number, digit), end=" ")
if digit > 5:
    print("and is greater than 5")
elif number == 0:
>>>>>>> 77e1c3e97fd4ce26a4883f0323741267dd7fcdc0
    print("and is 0")
else:
    print("and is less than 6 and not 0")
