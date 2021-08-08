"""Component 3 v1 - Compares the other products to the one last added
Created by Joshua Kan
02/08/2021
"""

# Intructions tell user how to use program
print("Welcome to the Item Comparison Program\n"
      "\nINSTRUCTIONS:"
      "\n - When entering the names of products, don't use numbers or symbols "
      "(e.g. 123, !@#)."
      "\n - When entering the weight of a product, only use don't type units "
      "and only present in grams."
      "\n - When entering the price of the product, make sure to not put more "
      "than 2 decimal places."
      "\n - When you are finished entering products, press X when it next "
      "asks you for the name of a product."
      "\n   Otherwise continue as normal."
      "\n")

product_details = []
product_name = ""

while product_name != "X":
    product_name = input("Please enter the name of the product: ")
    if product_name == "X":
        break

    else:
        product_weight = int(input("Please enter the weight/volume of the "
                                   "product: "))

        product_price = float(input("Please enter the price of the product: "))

        product_details.append([product_name, product_weight, product_price])

for item in product_details:
    print(f"\nItem Name: {item[0]}"
          f"\nItem Weight/Volume: {item[1]}g"
          f"\nItem Price: ${item[2]}0")



