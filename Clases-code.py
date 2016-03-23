
## code ##

class MyClass:
	number = 0
	name = "noname"

def Main():
	me = MyClass()
	me.number = 1337
	me.name = "Draps"
	
	friend = MyClass()
	friend.number = 3
	friend.name = "Steve"

	empty = MyClass()

	print("Name: " + me.name + ", Favorite Number: " + str(me.number))
	print("Name: " + friend.name + ", Favorite Number: " + str(friend.number)) 
	print("Name: " + empty.name + ", Fav Number: " + str(empty.number)) 

if __name__ == '__main__':
	Main()



## extra code ##


class MyNames:
	names = []
	
	#this is a method to add a new name to the 'names' list
	def add(self, name):
		self.names.append(name)

def Main():
	friends = MyNames() #create a object of MyNames and calls it 'list'
	
	#calling the add function/method to add new names to the list.
	friends.add("Draps")
	friends.add("Steve")
	friends.add("John")

	print("Names: " + str(friends.names))

if __name__ == '__main__':
	Main()





# TODO: Challenge\
# Create a class that holds a: \
# name, \
# age, \
# and a list of friends that can be 'add'ed too\

# Hint: The extra code will help with the friends list.


