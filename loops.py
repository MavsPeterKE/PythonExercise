#Using for loop to sum all even numbers for the range of 0-250
print("Using for loop to sum up all even numbers between 0-250")
sum = 0
for i in range(9,250):
    if (i%2==0):
        sum+=i
print("Total Sum for Even numbers in the range 9:250 %d"%sum)

#Loop through a list item String printing each on new line
print("\nUse for loop to loop through a list string item and print each string character using Nested Loops")

#Create a list of name
name_list = ["Danacana","Linet","Wanyonyi","Mitronbin","Exzhai"]

#Loop through list to acccess items
for item in name_list:
   for string_character in item:
       print(string_character)

#Using break (exits the loop if condition is true)
print("\nUsing break to stop looping once condition is met")
count = 0
for item in name_list:
	count+=1
	if(item=="Linet"):
		break
print("\nMitronbin Found at : %d"%count)


#Using Continue keyword
print("\nUsing continue keyword on For Loop ")
for i in range(1,100):
   if i==3:
       continue
print(i)


#Using While loop to print List Items
print("\nUsing While Loop to Print List Items")
i=0
while i<len(name_list):
	i+=1
	print(name_list[i-1])


#Get both list item and index using For loop
print("\nUsing enumerate in For loop and Getting both the list item and the index:")
for i,name in enumerate(name_list):
	print("List Item Position: %d"%i+" value: %s"%name)


for charecter in "petrr":
    print(charecter)

    	