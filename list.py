#list are used o store multiple iteams" in a single variables
myList = ["apple ", "banana" ,"cherry" , "orange" , "kiwi", "mango" , "apple" ]
print(myList)
#it allow dublicate values and it is changeable 
#it can store any data type 
print(myList[1:5])
print(myList[2])
print(myList[-3: -1])

# we can also chnge the value of list 
myList[1:4] = ["grape","peach","pear"]
print(myList)

#we can also add new value in list 
myList.append("watermalon")
print(myList)

#we can also insert new value 
myList.insert(2,"blueberry")
print(myList)

#we can also remove value from list 
myList.append(2,"watermalon")
print(myList)

#add any extendable value int list
myList2 = ["pineapple","cherry" , " blackberry"] 
myList.extend(myList2)
print(myList)