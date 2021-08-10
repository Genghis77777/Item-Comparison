"""Final Finished Program - includes notes and annotations.
11/08/2021
Created by Joshua Kan
"""

# Intructions tell user how to use program
print("Welcome to the Item Comparison Program\n"
      "\nINSTRUCTIONS:"
      "\n - When entering the names of products, don't use numbers or symbols "
      "(e.g. 123, !@#)."
      "\n - When entering the weight of a product, only use don't type units "
      "and only present in kilograms."
      "\n - If the product is measured in litres, enter it as normal."
      "\n - When entering the price of the product, make sure to not put more "
      "than 2 decimal places."
      "\n - When you are finished entering products, press X when it next "
      "asks you for the name of a product."
      "\n   Otherwise continue as normal."
      "\n")

# Collects amount of money user would like to spend on the entered items
money = float(input("Please enter the amount of money you would like "
                    "to use: $"))

# Variables and Lists for holding item details and values
product_details = []
product_name = ""
product_status = ""
best_value = []
worst_value = []

# While loop enables multiple products to be entered
while product_name != "X":
    # Creates an option for the input of a product name.
    product_name = input("\nPlease enter the name of the product: ")
    # If the user chooses to exit the program rather than continue,
    # they must enter "X"
    if product_name == "X":
        break
    # Otherwise the user is given the option of inputing its weight and price.
    else:
        product_weight = float(input("Please enter the weight/volume of the "
                                     "product: "))

        product_price = float(
            input("Please enter the price of the product: $"))
        product_price = round(product_price, 2)

        # Calculates unit price, and rounds it to 2dp
        unit_price = product_weight / product_price
        unit_price = round(unit_price, 2)

        # Adds the details described above to the product_details list
        product_details.append([product_name, product_weight, product_price,
                                unit_price])

# Prints the items and details in an orderly list for user to read.
for item in product_details:
    print(f"\nItem Name: {item[0]}"
          f"\nItem Weight/Volume: {item[1]}kg"
          f"\nItem Price: ${item[2]}0"
          f"\nUnit Price: ${item[3]}")

    # Determines the best valued item
    if len(best_value) == 0:
        best_value = item
    elif item[3] < best_value[3]:
        best_value = item

    # Determines the worst valued item
    if len(worst_value) == 0:
        worst_value = item
    if item[3] > worst_value[3]:
        worst_value = item

# Calculates the difference in value, between best and worst valued items
difference = worst_value[3] - best_value[3]
# Calculates the difference between money of user and best valued item
difference_money = best_value[2] - money

# Displays the user with the best and worst valued items
print(f"\nThe best valued item is {best_value[0]}")
print(f"The worst valued item is {worst_value[0]}")

# Recommends best valued item if it costs less than the money the user wishes
# to spend
if best_value[2] <= money:
    print(f"\nI recommend that you buy {best_value[0]}, as its unit price is "
          f"${difference} less than the unit price of {worst_value[0]}."
          f"\nAnd it fits with in your price range."
          f"\n\nThank you for using the Item Comparison Program."
          f"\nGoodbye!")
# Doesn't recommend the best valued item if it costs more than the money the
# user wishes to spend
else:
    print(f"\nI recommend that you buy {best_value[0]}, as its unit price "
          f"${difference} less than the unit price of {worst_value[0]}."
          f"\nHowever it costs ${difference_money} more than the amount you have,"
          f"\ntherefore perhaps this may not the best item for you."
          f"\n\nThank you for using the Item Comparison Program."
          f"\nGoodbye!")
