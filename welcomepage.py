# Welcome to our social network project! Let's use the tools we know to perform some actions.

# First, we'll display a welcome message to the user
# and write the name of the network.

# Next, we'll ask the user for some data to build their profile,
# and we'll save this information in variables.

# Finally, we'll print on the screen all the data we have collected, and allow
# the user to write a status message.

# I invite you to examine the code, read the comments, and understand the data types
# we are using in each case.

# To learn a little more about the user, we'll ask for some data.
# For example, their year of birth, and we'll use this data to find out the user's age.
# How will we do it? We'll use a variable to store the result of the age calculation.
# This is an integer data type.

# Next, we'll ask the user for their height in meters. This is a float data type,
# and we'll use this information to calculate the height in centimeters.

# Finally, we'll print on the screen all the data we have remembered about the user using print,
# and we'll ask them to write a message to display on the screen.

############################################################
# The first thing we'll do is write a welcome message to the user
# with the name of the network. You can modify this message to represent the name of your own network
# Note that by using """ we are also delimiting a string, but by doing it this way,
# line changes that occur in the code will be considered part of the string.
# If you're not convinced, try changing the delimiters to "

print("Welcome to ... ")
print("""
 ___    __       ___  ___  __   __  
|__  | / _` |__|  |  |__  |__) /__` 
|    | \__> |  |  |  |___ |  \ .__/ 
                                    
 ___    __       ___                
|__  | / _` |__|  |                 
|    | \__> |  |  |       

""")

# First interaction. We ask the user to enter their name,
# and we save it in a variable of type str
name = input("To start, tell me your name. ")
print()
print("Hello", name, ", welcome to My Network")
print()

# Second interaction. We ask for the entry of the year, and we use this
# data to estimate the person's age. Why do we say we are only "estimating" their age?
# What happens if we remove the 'int' data type conversion from the next line?
year = int(input("To prepare your profile, tell me in which year you were born. "))
age = 2017 - year - 1
print()

# Third interaction. We ask for the height, measured in meters.
# We use the 'float' conversion and an expression to convert this
# to a measurement in meters and centimeters.
height = float(input("Tell me more about yourself to add it to your profile. How tall are you? Tell me in meters. "))
height_m = int(height)
height_cm = int((height - height_m) * 100)

# Fourth interaction. We ask the user how many friends they have.
num_friends = int(input("Very well. Finally, tell me how many friends you have. "))

# With the collected data, we write on the screen a text that summarizes the obtained data
print()
print("Very well,", name, ". So we can create a profile with this data.")
print("--------------------------------------------------")
print("Name:  ", name)
print("Age:    ", age, "years")
print("Height:", height_m, "meters and", height_cm, "centimeters")
print("Friends:", num_friends)
print("--------------------------------------------------")
print("Thank you for the information. We hope you enjoy My Network")
print()

#                  HEADS UP!!!
# my code here    
# Request gender , ph number , city , state and country , 
gender = input("Whats your gender? ")
print()
print("--------------------------------------------------")
print(name, "is a: ", gender)


ph_number = input("Whats your phone number? ")
print()
print("--------------------------------------------------")
print(name, "phone number is: ", ph_number)

city = input("Whats your city? ")
print()
print("--------------------------------------------------")
print(name, "is at: ", city)

state = input("Whats state is that in? ")
print()
print("--------------------------------------------------")
print(name, "in the state of: ", state)

country = input("Whats country is that in? ")
print()
print("--------------------------------------------------")
print(name, "in the country of: ", country)


# Finally, we request a test message that serves to publish a user's status.
message = input("Now we are going to publish your first message. What do you think today? ")
print()
print("--------------------------------------------------")
print(name, "says:", message)
print("--------------------------------------------------")

# Now you can practice by requesting more data from the user. You just have to use input() and print()
# 1. Write 3 requests for data from the user, for example gender, phone number, city where they live,
#    country of birth, address, etc. Save that data in variables of the appropriate type, and finally write them on the screen
#    using print. You can add as many lines as you need.
