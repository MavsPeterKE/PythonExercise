#Tuple is a collection which is ordered and unchangeble and written with () brackets
#Tuple is basically a read only List(immutable)
referees = ('Owen','JohmSnow','Michael Trio')
counts = (2,3,4,5,6,7,8,9,10,11,15)
print("Print all elements in a Tuple")
print(referees)


#Accessing item in a tuple
print("\nPrint the 2nd Item in a Tuple : %s"%referees[1])


#Changing Value of an Item in a Tuple: Tuple is unchangeable once created
print("\nTry Changing a value in a Tuple. It remains Unchangeable")
#new_referees[0]="Mike"
#print(new_referees)
#It Throws an error


#Loop through items of a tuple
for referee in referees:
    print("This is our Referee Today: %s"%referee) 

#Adding Items to a Tuple
#Once Tuple is created you cannot add items to hence its content cannot be changed

#Remove Items to a Tuple
#Once Tuple is created you cannot remove items to hence its content cannot be changed

#Finding Length of a tuple
print("\nThe length of referees tuple is : %s"%len(referees))


#Deleting a tuple
#del referees
print("\nReferee Tuple Deleted")


#Slicing Tuples: Geting specified range of values
print("\nThe Values in the count Tuple from 2-8 ")
print(counts[2:8])


#Slice Tuple in reverse
print("Slicing Tuple in Reverse")
print(counts[::-1])


#Advanced slicing - Slice only even numbers in give range
print("\nSlicing by specifying how the tuple index should increment")
print("\nOriginal List")
print(counts)
print("\nSliced List by form the range 1:6 by incrementing the index by 2")
print(counts[1:6:2])


#Operations on a tuple
#Combining / Adding multiple tuples
combined_tuple = referees+counts
print(combined_tuple)


#Check if a given value is on the tuple
print("\nIs 6 Found on the tuple :")
print(6 in combined_tuple)


#Multiplying the number of items in the tuple. Make them appear given number of times
print("\nMultiply the tuple 3 times")
print(combined_tuple*3)


#Find maximam value in a tuple
print("\nThe maximum value in Counts Tuple is % d"%max(counts))


#Find maximam value in a tuple
print("\nThe minimum value in Counts Tuple is % d"%min(counts))
