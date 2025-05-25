
x = int(input("Entre the x : "))
if x > 50:
    print(x, "is is greter than 50")
elif x < 50:
    print(x,"is less than 50")
else:
    print(x, "is equal to 50")
    
age = int(input("Enter your age: "))

# Check for invalid age using 'not' and logical grouping
if not (age >= 1 and age <= 120):
    print("Invalid age entered")
# Check if age is between 1 and 17 (can't vote)
elif age >= 1 and age < 18:
    print("Can't vote")
# Check if age is 18 or older (can vote)
elif age == 18 or age > 18:
    print("Can vote")
# check if age is exctly 18
else:
    print("You r exactly u can vote")
    
    
     