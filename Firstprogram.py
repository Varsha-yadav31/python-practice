print("Hello World")

def print_name():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

def print_odd_even():
    number = int(input("Please enter your number: "))
    if(number % 2 == 0):
        print("Your number is even!")
    else:
        print("Your number is odd!")

# Call both functions
print_name()
print_odd_even()
