"""Component 2 - List for adding products and details
Collects name, weight and price of product, then prints them
Created by Joshua Kan
29/07/2021
"""

product_name = input("Please enter the name of the product: ")

product_weight = int(input("Please enter the weight/volume of the product: "))

product_price = float(input("Please enter the price of the product: "))

product_details = [[product_name], [product_weight], [product_price]]

print(product_details)

