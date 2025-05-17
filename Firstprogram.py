print("hlo world")

def print_name():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

# Call the function to run it
print_name()


def print_odd_even():
    number = int(input("please enter your number: "))
    if(number%2 == 0):
        print("your number is even!")
    else:
        print("your number is odd!")

print_odd_even()