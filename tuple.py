# tuple is used to store multiple items in a single variable like a list 
#but it is unchangable and it is in () this bractket and list is used []
mytuple = ("apple", "banana", "cherry")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
  
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
#join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found
