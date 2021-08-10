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

        product_price = float(input("Please enter the price of the product: $"))
        product_price = round(product_price, 2)

        unit_price = product_weight/product_price
        unit_price = round(unit_price, 2)


        product_details.append([product_name, product_weight, product_price,
                                unit_price, product_status])

for item in product_details:
    print(f"\n{item[4]}"
          f"\nItem Name: {item[0]}"
          f"\nItem Weight/Volume: {item[1]}kg"
          f"\nItem Price: ${item[2]}"
          f"\nUnit Price: ${item[3]}")
    if len(best_value) == 0:
        best_value = item
    elif item[3] < best_value[3]:
        best_value = item

    if len(worst_value) == 0:
        worst_value = item
    if item[3] > worst_value[3]:
        worst_value = item

print(f"\nThe best value item is {best_value}")
print(f"The worst value item is {worst_value}")


