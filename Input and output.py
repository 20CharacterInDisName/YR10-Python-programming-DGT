# Input and output
# Author: Joash Sayo
# Date: 3/05/2024
# Version: 1

username = input("What is your name? ")
print ("Your username is: " + username)

chosen_number = int(input("What is your chosen number? "))

# gets the chosen operation for chosen_number
doublen = chosen_number * 2
halfn = chosen_number / 2
squaren = chosen_number * chosen_number

operation = input("Pick your operation, double, half, square  ")
if operation == "double":
    print (doublen)
if operation == "half":
    print(halfn)
if operation == "square":
    print (squaren)