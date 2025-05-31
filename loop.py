"""Python Loops
Python has two primitive loop commands:

while loops
for loops"""

#while loop
count = 1
while count <=5:
  print("Gloal Ai Hub")
  count +=1





i = 1
while i < 6:
  print(i)
  i += 1
  
#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
# Print numbers from 1 to 100 using for loop
print("Numbers from 1 to 100 using for loop:")
for i in range(1, 101):
    print(i)
print("-" * 40)

# Print numbers from 1 to 200 using while loop
print("Numbers from 1 to 200 using while loop:")
j = 1
while j <= 200:
    print(j)
    j += 1
print("-" * 40)

# Print the multiplication table of a number
n = int(input("Enter a number to print its table: "))
print(f"Multiplication Table of {n}:")
for k in range(1, 11):
    print(f"{n} * {k} = {n * k}")
print("-" * 40)

# Print squares using for loop
print("Squares from 1 to 10 using for loop:")
for a in range(1, 11):
    print(f"{a}^2 = {a * a}")
print("-" * 40)

# Print squares using while loop
print("Squares from 1 to 10 using while loop:")
b = 1
while b <= 10:
    print(f"{b}^2 = {b * b}")
    b += 1
print("-" * 40)

# Print elements from a list using while loop
n_list = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("Printing list elements using while loop:")
j = 0
while j < len(n_list):
    print(n_list[j])
    j += 1
print("-" * 40)
