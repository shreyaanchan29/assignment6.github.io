# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Get the quantity of units purchased from the user
quantity = int(input("Enter the quantity of units purchased: "))
unit_cost = 100
total_cost = quantity * unit_cost
if total_cost > 1000:
 discount = total_cost * 0.1
 total_cost -= discount

print("Total cost of purchase: $", total_cost)