#Set Refers to collection which is unordered and unindexed. No duplicates
#Immutable data type can be an element of a set . Mutable Cannot

#Cn Python, when you initialize an object as word = {} you're creating a dict object and not a set objec therefore use set()
depot_locations = set()
vehicles = []
vehicles.extend(["KBJ","KCH","KBY"])


#Add Item to the set
print("Adding Items to the set using add(): ")
depot_locations.add("Tatu")
depot_locations.add("Thika")
depot_locations.add("Naivasha")
depot_locations.add("Nanyuki")
depot_locations.add("Kisumu")


#Try adding list to the set
depot_locations.update(vehicles)


#Print Set
print(depot_locations)


#Trying to add immutable data types as elemnts of a set
print("\nAttempt to add mutable type as an element of a set throws: unhashable type: 'list ")
# roles_set = set([{"name":"John","age":20},"2","3","4"])
# print(roles_set)
# Attempt to add list throws unhashable type: 'list'
# Attempt to add dictionary throws unhashable type: 'list'


#Print individual items within a set
print("\nUsing For Loop to print items in the set")
for location in depot_locations:
	print(location+"\n")


#Adding more than one item to the set using update()
print("\nAdding more than one item to the set using update()")

#Make sure to enclose the items to be added to the set with []
depot_locations.update(["Nairobi","Kisumu","Loliandi","Tamara"])
print(depot_locations)


#Remove Item from the set
depot_locations.remove("Naivasha")
depot_locations.discard("Nairobi")
print("\nRemove Naivasha (remove()) and Nairobi (discard())From the set")
print(depot_locations)


#Create set using set() constructor
depot_supervisors = set(("Linet","Owen","Tranui","Bantu","Lintu","Shnit"))
print("\nSet created using set() Constructor")
print(depot_supervisors)


#Add the content of one set to the other
print("\nCombine the contents of two sets into one")
print("Agents and Depots Sets Combined into One with an Intentional duplicate of Kisumu")
depot_locations.update(depot_supervisors)
print(depot_locations)


#Check if item is present on the set
print("Check if a given value is on the Set lists")
if "Tatu" in depot_locations:
	print("\nTatu is on Depots")
else:
	print("\nTatu is not in the Depots")
print("\nAdd Tuple to a set")
agents={"Maina","OLiech","John"}
service_areas = {"Kinoo","Kikuyu","Lutwami,"}
agents.update(service_areas)
print(agents)


#Create two list
regions = set(["Namib","Tala","Bent","Naiga","Rwanda","Kitale"])
regions_sumplement = set(["Namib","Eldoret","Gerntry","Juja","Tala","Kitale","Rwanda","Naiga"])


#Union (|)of the two sets (include items from both sets)
print("\nUnion of set Regions and Region Supplement is : Shows Items in both sets")
print(regions.union(regions_sumplement))
print(regions|regions_sumplement) #- Can also be written this ways


#Intersection of the two sets (show only item that appears in both sets)
print("\nIntersection of set Regions and Region Supplement is : Only shows items on both sets")
print(regions.intersection(regions_sumplement))
print(regions&regions_sumplement) #- can also be written this way


#Difference compares items in one set to the other and list the ones not appearing on the set
print("\nDifference of set Regions and Region Supplement is : shows items that appear on Regions and Not on Regions Supplement Set")
print(regions.difference(regions_sumplement))
print(regions-regions_sumplement) #Can also be written this way
print("\nDifference between sets Region Supplement Set and Regions Set: shows items that appear on Regions Supplement and Not on Regions Set")
print(regions_sumplement-regions)


#Symetric Difference compares items in one set to the other and list the ones not appearing on the set
print("\nThe Symmetric Difference between Regions Supplement and Regions: Shows Items that appear on both sets disctinctively")
print(regions_sumplement.symmetric_difference(regions))
print(regions^regions_sumplement) #Can also be written this way

