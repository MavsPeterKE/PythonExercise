#A list of Random numbers
numbers_list = [2,5,7,3,4,5,89,0,50,4,67,4,63,62,84]
even_numbers_list = []

#print all items in the list
print("All List Items")
print(numbers_list)

#access list item at specific position by index
value_at_pos3 = numbers_list[2];
print("\nList at Position 3 is : %d "%value_at_pos3)

#access list elements in a given range and print
print("\nList items in the range 4--8: ")
print(numbers_list[4:8])


#Looping through a list checking if cndition is true and adding items to a new list 
for number in numbers_list:
    if (number%2==0):
    	even_numbers_list.append(number)
print("\nAll even numbers added to a new list")
print(even_numbers_list)

#Adding more than one element to the list., They are all appended at the end of the list 
print("\nmore than one element added to the list")
even_numbers_list.extend([200,400,600,800,100])
print(even_numbers_list)


#Check if Item is in the list
if 1000 in even_numbers_list:
	print("\nYes 1000 is in the list ")
else:
	print("\nNo One Thousand is not in the list")




