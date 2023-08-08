# Split string method
# random
import random

set = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
x=len(set)
print(x)
value_1 = random.randint(0, x-1)
value_2 = random.randint(0, x-1)
value_3 = random.randint(0, x-1)

capitalletter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
y=len(capitalletter)
z=random.randint(0, y-1)
s=random.randint(0,y-1)
b=capitalletter[s]
a = capitalletter[z]

smallletter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
e=len(smallletter)
f=random.randint(0, e-1)
g=random.randint(0, e-1)
h=smallletter[g]
i = smallletter[f]

print(f"Your token code is {h} { value_1} {b} {value_2} {i} {value_3} {a} ")