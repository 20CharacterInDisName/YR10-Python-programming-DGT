# Fence cost calculator
# Author: Joash Sayo
# Date: 5/06/2024

restart = ""

#
def float_num_check(question):

    error = "Please enter a number over zero\n" 
    while True:  
            
            try:
                #Asks for a number
                response = float(input(question))

                #Makes sure the input is a number over 0
                if response > 0:
                    return response
                else:
                    #Otherwise it will print an error
                    print(error)

            except ValueError: 
                print(error)

# Main calculator

while restart == "":
    # Asks for inputs
    width = float_num_check("Enter the width:   ")
    length = float_num_check("Enter the length:   ")
    costpermeter = float_num_check("Enter the cost per meter:   ")

    # Calculate the perimeter
    perimeter = 2*(width+length)

    # Displays the perimeter, cost and asks to restart 
    print("Perimeter is",perimeter)
    print ("Cost is",perimeter*costpermeter)
    restart = (input("Enter to start again"))
    