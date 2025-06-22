#print then element [1 ,4,9,16,25,36,49,64,81,100]
n = 1
while n <= 10:
    print(n*n)
    n += 1
    
#print smae number index
num = [1,2,3,4,5,6,7,89,10]
indx = 0
while indx <= len(num):
    print(indx)
    indx += 1
    
    
    
#search for any number in list
num = [1,3,4,5,6,7,8,9,22 ,44,55]
x = int(input("Entre a number: "))
i = 0
while i < len(num):
    if(num[i] == x):        
        print(i)
    i += 1
        
    