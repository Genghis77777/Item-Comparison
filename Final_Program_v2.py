"""Full Program v2 - Final finished program, includes feedback
18/08/2021
Created by Joshua Kan
"""

# Intructions tell user how to use program
print("Welcome to the Item Comparison Program\n"
      "\nINSTRUCTIONS:"
      "\n Now, this program is for comparing two items that are the same "
      "product\n but may vary in price or weight. \n"
      "\n When you open the program you will be given these instructions, "
      "\n make sure to read through them before continuing into the program."
      "\n\n First you will enter the amount of money you would like to use for"
      "\n purchasing your product.\n"
      "\n Then you are asked to enter the name of the product "
      "\n (press enter when you are done), then its weight"
      "\n (don't include kgs/L), then enter its price.\n"
      "\n After that you have the choice to enter another product, you can "
      "\n enter as many products that you want.\n"
      "\n Here are some extra instructions that are very important before "
      "proceeding:"
      "\n - When entering the names of products, don't use numbers or symbols "
      "(e.g. 123, !@#).\n"
      "\n - When entering the weight of a product, don't enter any units "
      "\n   and only present in kilograms (but don't write kgs, e.g. 1 not "
      "1kg).\n"
      "\n - If the product is measured in litres, enter it as normal.\n"
      "\n - When entering the price of the product, make sure to not put more "
      "than 2 decimal places.\n"
      "\n - When you are finished entering products, press X when it next "
      "asks you for the name of a product."
      "\n -------------------------------------------------------------------")

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
while product_name != "x":
    # Creates an option for the input of a product name.
    product_name = input("\nPlease enter the name of the product: ")
    # If the user chooses to exit the program rather than continue,
    # they must enter "x"
    if product_name == "x":
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
          f"\nHowever it costs ${difference_money} more than the amount you "
          f"have,"
          f"\ntherefore perhaps this may not the best item for you."
          f"\n\nThank you for using the Item Comparison Program."
          f"\nGoodbye!")
