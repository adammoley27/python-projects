from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))


n=1==2
print(n)

a= 6
print(a)
while a>2:
        print("A is greater than 2 still")
        print(a)
        a-=1
        print(a)
        
    
    
def play(a,b):
    c = (a+b)
    print(c)

play(9,9)


def play(a,b):
    c = (a*b)
    print(c)
    
play(9,9)

def play(a,b):
    c = (a-b)
    print(c)
    
play(9,9)

def play(a,b):
    c = (a/b)
    print(c)
    
play(9,9)


from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine

print(machine())


from platform import processor

print(processor())

from platform import system

print(system())

from platform import version

print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
