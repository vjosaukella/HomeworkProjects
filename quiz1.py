# Ask user for two numbers
print("Your goal is to find two numbers with the same product and sum!")
number1 = input("What is your first number?")
number2 = input("What is your second number?")
sum = int(number1) + int(number2)
product = int(number1) * int(number2)
print("Your sum is..." + str(sum))
print("Your product is..." + str(product))
# Create a loop that does the following until the product and sum are the same
while (product != sum):
    #If your sum and product are not equal, tell the user
    print("That is not right!")
    print("Please try again.")
    # otherwise ask for two more numbers
    number1 = input("What is your first number?")
    number2 = input("What is your second number?")
    # Calculate and disply their sum
    sum = int(number1) + int(number2)
    print("Your sum is..." + str(sum))
    # Calculate and display their product
    product = int(number1) * int(number2)
    print("Your product is..."+str(product))
print("Good work! Your sum and product are equal!")


