# Conversion rate calculator
# Author: Joash Sayo
# Date: 19/06/2024
# Version: 1.3

# Function that makes sure the input is over 0 and a number
repeat = ""
while repeat == "":

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


# Asks for the mode (time, distance or mass)

    correctconverion = False
    while correctconverion == False:
        mode = input("What mode would you like? (time, mass or distance):  ")

        if mode == "mass":
            print("Mode is mass\n")
            correctconverion = True
        # elif chain
        elif mode == "distance":
            print("Mode is distance\n")
            correctconverion = True

        elif mode == "time":
            print("Mode is time\n")
            correctconverion = True
        else:
            print("Error, unknown conversion rate | please enter a valid conversion rate\n")
            correctconverion = False


    # Dictionary for distance
    if mode == "distance":
        converstion_dictionary_distance = {
            "nm": 1e+9,
            "mm": 1000,
            "cm": 100,
            "m": 1,
            "km": 0.001
        }
    # Dictionary for time
    elif mode == "time":
        converstion_dictionary_distance = {
            "day": 0.00069444583333,
            "hour": 0.0166667,
            "min": 1,
            "mins": 1,
            "second": 60,
            "seconds": 60,
            "pictosecond": 6e+13
        }
    # Dictionary for mass
    elif mode == "mass":
        converstion_dictionary_distance = {
            "mg": 1e+6,
            "g": 1000,
            "kg": 1,
            "t": 0.001
        }

    # Gets the user's inputs, if its a number it runs it though the float_num_check function
    amount = float_num_check("give a number: ")
    from_unit = input("from what unit: ")
    to_unit = input("to what unit: ")


    # Multiply to get the value
    multiply_by = converstion_dictionary_distance[to_unit]
    standard = amount * multiply_by

    # Divide to get the value
    divide_by = converstion_dictionary_distance[from_unit]
    answer = standard / divide_by

    # Prints the answer
    print(f"There are {answer} {to_unit} in {amount} {from_unit} ")

    # If the user would like to try again
    repeat = input("\nPress enter to go again\n")