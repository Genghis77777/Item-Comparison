"""Component 4 - v1 Recommends which product to buy
Initial version only indentifies most expensive and cheapest products
09/08/2021
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

product_details = []
product_name = ""
product_status = ""
best_value = []
worst_value = []

while product_name != "X":
    product_name = input("\nPlease enter the name of the product: ")
    if product_name == "X":
        break

    else:
        product_weight = float(input("Please enter the weight/volume of the "
                                     "product: "))

        product_price = float(
            input("Please enter the price of the product: $"))
        product_price = round(product_price, 2)

        unit_price = product_weight / product_price
        unit_price = round(unit_price, 2)

        product_details.append([product_name, product_weight, product_price,
                                unit_price, product_status])

for item in product_details:
    print(f"\n{item[4]}"
          f"\nItem Name: {item[0]}"
          f"\nItem Weight/Volume: {item[1]}kg"
          f"\nItem Price: ${item[2]}0"
          f"\nUnit Price: ${item[3]}")

    if len(best_value) == 0:
        best_value = item
    elif item[3] < best_value[3]:
        best_value = item

    if len(worst_value) == 0:
        worst_value = item
    if item[3] > worst_value[3]:
        worst_value = item

print(f"\nThe best valued item is {best_value[0]}")
print(f"The worst valued item is {worst_value[0]}")

