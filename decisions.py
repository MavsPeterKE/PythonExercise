#Variables to hold data
days = 5
unit_count = 0
units = ['Algorithimns','File Streams','Encryption','Network Comm','Flask']
days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday']

#Run only one block is condition is true
print("Print only one if True")
if (2>3):
	print("True")
else:
	print("False")


#Running Concurrent Decisoon
print("Check All conditions at the same time")
if (2>3):
	print("peter is ")
if(3>2):
	print("Mike")
if (2>1):
	print("Joan")


#Executing only one if condition is true. This means only one block under the elif is executed
print("Print only one if True")
if (days <7):
	print("peter")
elif(days == 5):
   	print("Mike")
elif (days >4):
    print("Joan")
else:
    print("Out of Range")


	

    


