groceries = []
prices = []

print("\n--- Welcome to the Shopping Cart ---\n")

while True:
    item = input("Enter the grocery item to buy (q to quit): ")

    if item.lower() == 'q':
        break

    try:
        price = float(input(f"Enter the price of '{item}': Rs "))
        groceries.append(item)
        prices.append(price)
    except ValueError:
        print("Please enter a valid number for price.\n")

print("\n---------- Your Cart ----------\n")
print(f"{'Item':<20} {'Price (Rs)':>10}")
print("-" * 30)

for i in range(len(groceries)):
    print(f"{groceries[i]:<20} {prices[i]:>10.2f}")

total = sum(prices)
print("-" * 30)
print(f"{'Total':<20} {total:>10.2f}")