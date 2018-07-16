#Create list
cars = ['Maruti','Honda','BMW']
print("#"*20)
print (cars[0])

num = [100,20,30,30.6,96]
sum = num[1] * num[4]
print(sum)

#List is a collection of data of any type. List's are mutable.
#Change list values
cars[0] = 'Ambasidor'
cars[1] = 'fiat'
print(cars)

#Add items to the list using append. It adds at the end of the list item
cars.append('Benz')
print(cars)

#Add items to the list using insert. It adds at the location specified
print("#"*40)
cars.insert(1,'Audi')
print(cars)

#Find the index of the item
print("#"*40)
print(cars.index('Audi'))


#Remove the items from the list using pop. This wil remove the items from the end of the list.
# Similar to append, its adds in the end and pop removes from the end.
print("#"*40)
print(cars.pop())

#Remove itsm fro the list of our desire
print("#"*40)
cars.remove('fiat')
print(cars)
print(cars)

#Slice the list
print("#"*40)
print(cars[1:2]) # first argument is the array value and the second one is the count.

#Sort
print("#"*40)
cars.sort()
print(cars)