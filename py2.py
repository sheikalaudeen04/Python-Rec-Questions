def generate_bill(items):
    total_amount = 0
    print("*******************")
    print("Retail Bill")
    print("*******************")
    print("Item\t\tPrice\tQuantity\tTotal")

    for item, details in items.items():
        price = details['price']
        quantity = details['quantity']
        item_total = price * quantity
        total_amount += item_total

        print(f"{item:<15}{price:<10.2f}{quantity:<15}{item_total:<10.2f}")

    print("\nTotal Amount: ", total_amount)


items = {}
print("Enter 'exit' to finish adding items.")
while True:
    item_name = input("Enter item name: ")
    if item_name.lower() == 'exit':
        break
    item_price = float(input("Enter item price: "))
    item_quantity = int(input("Enter quantity: "))
    items[item_name] = {'price': item_price, 'quantity': item_quantity}
            
generate_bill(items)


