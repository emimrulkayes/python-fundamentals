# We can create our own function called hello as follows:
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)



"""------------------------------
We can further improve our code:
---------------------------------"""
# Create our own function
def hello(to):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)



"""
We can change our code to add a default value to hello:
"""
# Create our own function
def hello(to="world"):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()



"""
The following very small modification will call the main function and restore our program to working order:
"""
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(to="world"):
    print("hello,", to)

main()



"""
Effectively, x is passed to square. Then, the calculation of x * x is returned back to the main function.
"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n


main()


