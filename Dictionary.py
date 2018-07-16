# Dictionary is a key value pair data type. Not sequenced and no indexing.
car = {'Make':'Benz', 'Model':'A00B1','Year':'2018'}
print (car)

car['colour'] = 'Red'
print (car)

#dictionaries are always accessed by keys and not by index value
#print(car['Make'])

# Create a empty dictionary an assign value to it
print("#"*30)
number = {}
print (number)

number['First number'] = 'One'
number['Second number'] = 'Two'
number['Third number'] = 'Three'

print (number)

# Get the list of keys in the car
print("----- List the Keys -----")
print(car.keys())
print("----- List the Items -----")
print(car.items())
print("----- List the Values -----")
print(car.values())

