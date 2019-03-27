#List is a collection which is ordered and mutable and written with [] brackets
#A list of Random numbers
numbers_list = [2,5,7,3,4,5,89,0,50,4,67,4,63,62,84]
even_numbers_list = []


#print all items in the list
print("All List Items")
print(numbers_list)


#access list item at specific position by index
value_at_pos3 = numbers_list[2]
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


#Delete one item from the list
print("\nOne Item deleted from the list")
del even_numbers_list[2]
print(even_numbers_list)


#Delete Multiple Items
print("\n Delete multiple items")
del even_numbers_list[4:6]
print(even_numbers_list)


#To delete item of a known value from the list use rremove
print("\nRemove Item of a known value")
even_numbers_list.remove(800)
print(even_numbers_list)


#Pop Element
print("\n Pop element at given position")
even_numbers_list.pop(1)
#print(even_numbers_list)


#Insert item at specified index
print("\nInsert Item at list Pos")
even_numbers_list.insert(2,400)
print(even_numbers_list)


#Print length of list
print("\nLength of list is %d"%len(even_numbers_list))


#Count occurence of given value in the list
print("4 has occurred %d times in the list"%even_numbers_list.count(4))


#Sort list in ascending order using sorted() -"Returns the list"
print("\nSorted List of even numbers in ascending order:")
print(sorted(even_numbers_list))


#Sort list in descing order
print("\nSorted List of even numbers in descending order:")
print(sorted(even_numbers_list,reverse = True))


#Sort list using sort()
print("\nSorted List using the sort() in Ascending order:")
even_numbers_list.sort()
print(even_numbers_list)


#Sort list using sort()
print("\nSorted List using the sort(): in descending Order<")
even_numbers_list.sort(reverse = True)
print(even_numbers_list)





