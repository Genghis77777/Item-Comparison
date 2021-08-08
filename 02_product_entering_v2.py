"""Component 2 - List for adding products and details
v2 Collects name, weight and price of product,
Prints them individually
Created by Joshua Kan
02/08/2021
"""

product_name = input("Please enter the name of the product: ")

product_weight = int(input("Please enter the weight/volume of the product: "))

product_price = float(input("Please enter the price of the product: $"))

product_details = [[product_name], [product_weight], [product_price]]

print("Item Name: {}\n"
      "Item Weight/Volume: {}g\n"
      "Item Price: ${:.2f}".format(product_details[0][0], product_details[1][0],
                                   product_details[2][0]))
