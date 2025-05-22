#data type : int ,str,bool,float
#we can check data type by using print(type(x))
import random  # Corrected 'rendom' to 'random'
x = 4
y = 6.9
print(type(x))
print(type(y))
#convert data type into anotherdatatype
a = float(x)
b = int(y)
print(a)
print(b)
# to print any random number b/w 1 to 10
print(random.randrange(1, 10))  # Corrected 'rendom.rendrang' to 'random.randrange'
# casting means convert one datatype into another 
#such as from int to float from float to int so on 

# string 
#it is a collecion of charecters and it is immutable and i is in double or single quotes

e = "hello"
f ='world'
print(e)
print(f)

# multiple line string 
# it is written in triple quotes 
#such as

h = """ i am varsha, i am from azamgarh,

i am student ofcomputer science and engineering  """
print(h)

# looping in string 
for x in "banana":
    print(x)