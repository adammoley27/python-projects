from random import random, seed

seed(0)

for i in range(5):
    print(random())
    

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
    
    
import random
dir(random)
print(dir(random))

