#Set Refers to collection which is unordered and unindexed. No duplicates

#Cn Python, when you initialize an object as word = {} you're creating a dict object and not a set objec therefore use set()
depot_locations = set()

#Add Item to the set
print("Adding Items to the sret using add(): ")
depot_locations.add("Tatu")
depot_locations.add("Thika")
depot_locations.add("Naivasha")
depot_locations.add("Nanyuki")

#Print Set
print(depot_locations)

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

#Check if item is present on the set
print("Check if a given value is on the Set lists")
if "Tatu" in depot_locations:
	print("\nTatu is on Depots")
else:
	print("\nTatu is not in the Depots")

#Add two tuples into a set
agents={"Maina","OLiech","John"}
service_areas = {"Kinoo","Kikuyu","Lutwami"}
agents.update(service_areas)
agent_service_areas = set(agents);
print(agents)

