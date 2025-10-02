##
# Code by Parker Jolly
# On 10/2/2025
# Program name: Kilometer Converter
##
def km_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

#Ask for input, run the function, and display, all in one line.
print("That's " + str(km_to_miles(float(input("Input a distance in kilometers to be converted into miles: ")))) + "miles.")
