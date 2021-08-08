"""Component 1, Input for money that user would like to spend
28/07/2021
Created by Joshua Kan
"""

money = float(input("Please enter the amount of money you would like "
                    "to use: "))

def component1():
    confirm = input(
        "Are you sure you want to use ${:.2f}? (Y or N):".format(money))
    if confirm == "Y":
        print("Next component")
        confirm = input("Do you want to continue? ")
    else:
        print("Okay")

component1()
