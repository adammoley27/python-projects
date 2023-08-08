def perimeter():
    length = x
    breath = z
    length_2 = x*2
    breath_2 = z*2
    units = y
    perimeterz = f"The perimeter of the rectangle is {length_2 + breath_2} {units}."
    return perimeterz

x = int(input("insert the length:  " "\n"))
z = int(input("insert the breath: " "\n"))
y = input("insert the units" "\n")

print(perimeter())

def zz ( firs, sec, zee ):
    o= firs/sec
    return (f" the division value is {o} {zee}")
    
x = int(input("insert the length:  " "\n"))
z = int(input("insert the breath: " "\n"))
y = input("insert the units" "\n")


print(zz(x,z,y))
