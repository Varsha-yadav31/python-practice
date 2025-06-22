#wap to print sum of 1st n number 
n = int(input("entre a number:"))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print(fact)
