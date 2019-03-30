#Object is a collection of data (variables) and methods (functions) that act on those data. 
#Class is a blueprint for the object.


#Doc String provides a convenient way of associating documentation with Python modules, functions, classes, and methods. 
#Doc String is written as the first line in a class, method, module or packaage


print("\nCreating Class Instance using Object")
#Defining a class in Python - use class Keyword


class Student:
	"""#A way to type a line that does nothing. Necessary because when defining a class you need atleast one line"""
	pass


#Creates an instance of Student class. (Object)
student1 = Student()
student1.name = "Jacinta"
student1.age = 30
student1.class_stream = "West Wing W"
student1.class_level = 4


#Printing Data from Student Class
print("%s"%student1.name+" is %d"%student1.age+" Years Old")
print("%s"%student1.name+" is in class %s"%student1.class_level+" %s"%student1.class_stream)


#Working with class feature [Methods, Initialization and help text]
print("\nUsing Class constructor __init__()")
#Defining a class in Python - use class Keyword
"""Teacher Class Contains Teacher attributes and related operations on Teacher"""


class Teacher:
    """This class Contains Attributes and Operations done on a teacher"""
	#Class initialization (Constructor)

    
    def __init__(self,name,subject_list,qualification,designation):
		self.teacher_name = name
		self.subject_list = subject_list
		self.qualification = qualification
		self.designation =designation
    

    def rank_index(self):
    	"""Computes and Returns the teacher Rank Index"""
    	index = len(self.subject_list)*3
    	return index


#Create instance of Teacher Class
teacher1 = Teacher("Peter Mike",["English","Kiswahili"],"Masters","Principal")


#Print values from the instance
print("%s"%teacher1.teacher_name+" has attained %s"%teacher1.qualification+" and is the %s"%teacher1.designation)
print("%s"%teacher1.teacher_name+" Has a ranking Index of "+"%d"%teacher1.rank_index())




help(Teacher)
help(Student)




