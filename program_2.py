##
# Code by Parker Jolly
# On 10/2/2025
# Program name: Math Quiz
##
import random


def main():
    while True:
        if input("Would you like to take a quiz? Y/N: ").lower().replace(" ","") == "y":
            quiz()
        else:
            print("Exiting program...")
            break

def quiz():   
    num1 = random.randrange(-2000,2000)
    num2 = random.randrange(-2000,2000)
    if float(input("What is " + str(num1) + " + " + str(num2) + "? ").replace(" ","").replace(",","")) == num1+num2:
        print("Yes! That is correct!")
    else:
        print("No. " + str(num1) + " + " + str(num2) + " = " + str(num1+num2) + ("."))


main()
