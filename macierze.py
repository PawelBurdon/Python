import numpy as np
from numpy import random

mac = int(input("Podaj ilsoc wierszy: "))

x = random.randint(10, size=(mac, mac))
y = random.randint(10, size=(mac, mac))

print(x)
print("\n")
print(y)

c = x + y

print("\n")
print(c)

a = x * y

print("\n")
print(a)