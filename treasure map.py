# 🚨 Don't change the code below 👇
row1 = ["⬜️ ","️⬜️","️⬜️"]
row2 = ["⬜️ ","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
vertical = int(position[0])
horizontal = int(position[1])

selectedrow = map[horizontal-1]
selectedcolumn= selectedrow[vertical-1]= "X"



# Write your code above this row 👆

# 🚨 Don't change the code below 👇

print(f"{row1}\n{row2}\n{row3}")
print(selectedcolumn)



