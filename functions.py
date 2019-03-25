#Functions - Give program an interface through which it can run program code without knowing the details about the program being run

# def functionName(paramenter1, parameter2=default_value):
# < code block >
# return value (optional)

number_input1 = 50
number_input2 = 60
name_length = 0
user_name = "Peter Onyango"


#Function that returns sum of two numbers with a parameter
def add_two_numbers(first_numerical_Value=0,second_numerical_value=0):
	return first_numerical_Value+second_numerical_value
total = add_two_numbers(number_input1,number_input2)


#Fuction that does not take a parameter and neithrr returns something
def set_name_length():
	name_length = len(user_name)


print("\nSum of  %d"%number_input1+" and %d"%number_input2+" is: %d"%add_two_numbers(number_input1,number_input2))





	