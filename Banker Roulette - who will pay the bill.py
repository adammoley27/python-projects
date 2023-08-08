# Split string method
# random
import random
names_string = input("Give me everybody's names, separated by a comma. \n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

display_nameslist = print(names)

#count the list and display
x =len(names)
print(x)

#pick random postion number of names from 0 to the number of list and display
random_choice = random.randint( 0, x-1)
print(random_choice)

#use the random choice to select a name from the list to pay
y = names[random_choice]

#print the name of the selected random choice
print (y)

print(f"{y} is goint to buy the meal today!")