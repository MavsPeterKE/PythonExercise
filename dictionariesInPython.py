#Dictonary is a collection which is unordered, Mutable and indexed. No duplicates

#Creating a Dictionary 
citizen_dictionary = {"name":"Peter","age":1, "phone":"+254"}
print("Print all dictionary items")
print(citizen_dictionary)

#Access Dictionary element by specific key using get() and ["key"]
print("\n Get dictonary value with the key 'name' :"+citizen_dictionary.get("name") +" And Age is %d"%citizen_dictionary["age"])

#Change value of item with a given key on the dictionary
print("\nChange dictionary item with the key 'age' to a new value")
print("Age before changing: %d"%citizen_dictionary.get("age"))
citizen_dictionary["age"]=26

print("Age After changing: %d"%citizen_dictionary.get("age"))

#loop through printing all dictionary keys
print("\nPrint all Dictionary Keys and use the key to get the value")
for key in citizen_dictionary:
    print("Dictionary Key : "+key+" Value of this key is")
    #print("The value for this key:"+citizen_dictionary.get(key))
    print(citizen_dictionary.get(key))

#Print both dictionary key and value using for loop
print("\nPrint Both Dictionary Keys and their Values ")
for key,value in citizen_dictionary.items():
    print(key+" ",value)

#Check if a specific key is on the dictionary
print("\nCheck if Agent Key is on the Dictionary")
if "agents" in citizen_dictionary:
    print("Yes 'agents' key is on the dictionary")
else:
	print("No 'agent' key not found")
# if citizen_dictionary.has_key("jambas"):
# 	print("Jambas Key is available")
# else:
# 	print("No Jambas Key")

#Get length of the Dictionary
print("\nThe length of the dictionary is % d"%len(citizen_dictionary))

#Adding Item to the dictionary: Hint- new key and assign value
print("\nAdding a new Key to the dictionary")
print("Dictionary before adding new key")
print(citizen_dictionary)
citizen_dictionary["crime_record"] = "None"
print("Dictionary After Adding new Key")
print(citizen_dictionary)

#Remove Item from the dictionary using pop("key")
print("\nRemove Crime Record from the dictionary")
citizen_dictionary.pop("crime_record")
print(citizen_dictionary)

#Remove last item on the dictionary popitem()
print("\nRemove Last Item From the Dictionary")
print("\nDictionary Before Removing Last Item")
print(citizen_dictionary)
citizen_dictionary.popitem()
print("\nDictionary After Removing Last Item")
print(citizen_dictionary)

#Use del to delete the whole dictionary
#Use clear() to clear the whole dictionary

#Using dict() Constructor to create a dictionary
print("Create Dictionary using dict() Constructor")
teams_dictionary = dict(couch="Alexandar",stadia="Stamford",trophies=16,referee="Alendar")
teams_dictionary["legends"] = 800
print(teams_dictionary)

#Get all keys from the dictionary
print("\nPrint all dictionary keys")
print(teams_dictionary.keys())

#Get all dictionary Values from the dictionary
print("\nPrint all dictionary keys")
print(teams_dictionary.values())

#Check if key has value
print("check if 'legends' key has value")
if teams_dictionary.has



