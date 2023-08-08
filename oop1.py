class French:
    def say_hello(self):
        print("Bonjour")
        
class Yoruba:
    def say_hello(self):
        print("Ekaro")
        
class Hausa:
    def say_hello(self):
        print("ina Kwuana")
        
def intro(lang):
    lang.say_hello()
    
    
adam = French()
john = Yoruba()
alhaji = Hausa()

intro(adam)
intro(john)
intro(alhaji)

# newline
print("\n")
class Car:
    def start(self):
        print("Engine started")
        
    def move(self):
        print("car is running")
        
    def stop(self):
        print("Brakes applied")
        
    def Display(self):
        print("Car Make displayed")
               
    def horn(self):
        print("Horn is On")
        
    def wiper(self):
        print("Wiper is working")
        
   
class Clock:      
    def move(self):
        print("Tick Tick Tick")
        
    def stop(self):
        print("Clock needles Stopped")
        
    def Display(self):
        print("Time is Displayed")
        
    def Off(self):
        print("Display is off")
        
    def Alarm(self):
        print("alarm started")
        
        
class Human:      
    def move(self):
        print("Walking home")
        
    def stop(self):
        print("Talking a rest")
        
    def Display(self):
        print("Human teeths showing")
        
    def Run(self):
        print("Running")
        
    def jogging(self):
        print("jogging")
        

def do_this(a):
    
    a.move()
    a.stop()
    a.Display()
    
    
car = Car()
clock = Clock()
person = Human()


do_this(car)
print("\n")
do_this(clock)
        
        
        
        