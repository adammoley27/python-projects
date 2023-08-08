# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nametype_1 = name1.lower()
nametype_2 = name2.lower()
print(nametype_1)
print(nametype_2)
t_n1 = (nametype_1.count('t'))+ (nametype_2.count('t'))
r_n2 = (nametype_1.count('r'))+(nametype_2.count('r'))
u_n3 = (nametype_1.count('u'))+(nametype_2.count('u'))
e_n4 = (nametype_1.count('e'))+(nametype_2.count('e'))
l_n5 = (nametype_1.count('l'))+(nametype_2.count('l'))
o_n6 = (nametype_1.count('o'))+(nametype_2.count('o'))
v_n7 = (nametype_1.count('v'))+(nametype_2.count('v'))
e_n8 = (nametype_1.count('e'))+(nametype_2.count('e'))

total_1 = t_n1+r_n2+u_n3+e_n4
total_2 = l_n5+o_n6+v_n7+e_n8


score = (int(f"{total_1}{total_2}"))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")