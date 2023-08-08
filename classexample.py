class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name + " is " +  str(self.age)
        
        
    def walk(self):
        print(self.name + " is walking home")
        
    def speak(self):
        print("Hello, My name is " + self.name + ". I , "  + self.name + " is " + str(self.age) + " .")
Human = Person("Tom", 12)
Human2 = Person("Zain", 7)

# To print the properties of the object
print(Human)
print(Human2)

print("\n")
print(Human.name)
print(Human.age)

print("\n")
print(Human2.name)
print(Human2.age)


# behaviour for classes and object
print("\n")
Human.walk()
Human.speak()

print("\n")
Human2.walk()
Human2.speak()