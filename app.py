# Example 1 - Creating a variable and printing it to the terminal
printedvar = "Hello World!"
print(printedvar)



# Example 2 - Crinting input taken from the user and converted to an integer
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
answer = number1 + number2

print(number1, "+", number2, "=", answer)



# Example 3 - Choosing what to do using an if statement
name = input("Please enter your name: ")

if name.lower() == "dave":
    print(f"I dont talk to people called {name}")
elif name.lower() == "simon":
    print(f"{name} is a great name!")
else:
    print(f"Hello {name}")