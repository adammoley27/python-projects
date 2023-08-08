from datetime import date

date_now = date.today()
print(date_now)
print(date_now.strftime("%Y %B %d %A"))
print(date_now.strftime("%A, %dth of %B. %Y"))

# newline
print("\t")
print("\n")
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)



# newline
print("\t")
print("\n")
import time
print(time.ctime())



# newline
print("\t")
print("\n")
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))


import calendar
print(calendar.calendar(2026))

import calendar
calendar.prcal(2027)

import calendar
print(calendar.month(2020, 11))


import calendar
print(calendar.weekheader(1))
    
import calendar
print(calendar.weekheader(2))

import calendar
print(calendar.weekheader(3))
    
import calendar
print(calendar.weekheader(4))
    
    


    