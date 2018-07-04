# Ask the Name
name = input("What is your name?: ")

# Ask for Age
age = input("What is your age?: ")

# Ask the City
city = input("Which city you are comming from?: ")

# Ask what they enjoy
love = input("What do you enjoy about?: ")

# Create output text
string = "Your name is {} and your age is {}. You live in {} and you enjoy doing {}"

# Print output to the screen
output = string.format(name, age, city, love)
print (output)

# Use Builtin functions from help

# Sample : a = "Part", b = 1 and a+b -> This will throw an error. This can be solved by a+str(b)

# format data
#a = "part"
#b = 1
#c = "{} - {}".format(a,b)
#print (c)