#Variables to hold data
days = 5
unit_count = 0
units = ['Algorithimns','File Streams','Encryption','Network Comm','Flask']
days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday']

#Running Concurrent Decisoon
if (days>3):
	print("peter")
if(3>2):
	print("Mike")
if (2>1):
	print("Joan")

#Executing only one if condition is true. This means only one block under the elif is executed
if (days <7):
	print("peter")
elif(days == 5):
   	print("Mike")
elif (days >4):
	print("Joan")

#Looping Through Values in a list
for unit in units:
	unit_count+=1
	print "Unit Taught is: %s" % unit
	

    


