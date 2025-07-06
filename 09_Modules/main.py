import datetime as dt
from math import pi, pow
import random
import math
import my_modules

welcome_message = my_modules.greet("Abdul Moiz")
print(welcome_message)

sum = my_modules.add(5, 10)
print(f"The sum of 5 and 10 is: {sum}")


print("📐 Square root of 16 is:", math.sqrt(16))
print("🎲 Random number between 1-100:", random.randint(1, 100))


print("🧮 Value of Pi:", pi)
print("2 to the power of 3:", pow(2, 3))


today = dt.date.today()
print("📅 Today's date is:", today)

print("🧰 Functions in math module:")
print(dir(math))
