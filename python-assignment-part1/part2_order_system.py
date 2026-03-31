### Task 1: Explore the Menu
##Print the full menu grouped by category
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# Get unique categories
categories = set(item["category"] for item in menu.values())

# Print menu grouped by category
for category in categories:
    print(f"\n===== {category} =====")

    for item, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"

            print(f"{item:<15} ₹{price:.2f}   [{status}]")

##Using dictionary methods
# Total number of items
total_items = len(menu)

# Total available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

# Items under ₹150
cheap_items = [(name, details["price"]) 
               for name, details in menu.items() 
               if details["price"] < 150]

print("\nSummary:")
print(f"Total items: {total_items}")
print(f"Available items: {available_items}")
print(f"Most expensive item: {most_expensive[0]} (₹{most_expensive[1]['price']})")

print("\nItems under ₹150:")
for name, price in cheap_items:
    print(f"{name} - ₹{price}")
# grouping menu items by category
# finding most expensive item using lambda


###Task 2 — Cart Operations
cart = []

## Function to add item
def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"{item_name} does not exist in menu.")
        return

    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable.")
        return

    # Check if item already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    # Add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{quantity} to cart")


## Function to remove item
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name} from cart")
            return

    print(f"{item_name} not found in cart")


## Function to print cart
def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(f"{item['item']} x{item['quantity']}")
    if not cart:
        print("Cart is empty")



## Simulation Steps


add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)  # should update quantity
print_cart()

add_to_cart("Mystery Burger", 1)  # does not exist
print_cart()

add_to_cart("Chicken Wings", 1)  # unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()



## Final Order Summary


print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price

    print(f"{item['item']:<18} x{item['quantity']}    ₹{total_price:.2f}")

gst = subtotal * 0.05
total = subtotal + gst

print("------------------------------------")
print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):               ₹{gst:.2f}")
print(f"Total Payable:          ₹{total:.2f}")
print("====================================")


### Task 3: Inventory Tracker


import copy

## Deep copy of inventory
inventory_backup = copy.deepcopy(inventory)

# Modify original inventory to prove deep copy
inventory["Paneer Tikka"]["stock"] = 5

print("\nChecking Deep Copy:")
print("Original Inventory (modified):", inventory["Paneer Tikka"])
print("Backup Inventory (unchanged):", inventory_backup["Paneer Tikka"])

# Restore original inventory
inventory = copy.deepcopy(inventory_backup)


## Order Fulfilment


print("\nProcessing Order...")

for item in cart:
    item_name = item["item"]
    qty_needed = item["quantity"]

    stock_available = inventory[item_name]["stock"]

    if stock_available >= qty_needed:
        inventory[item_name]["stock"] -= qty_needed
    else:
        print(f"⚠ Not enough stock for {item_name}. Only {stock_available} available.")
        inventory[item_name]["stock"] = 0


## Reorder Alerts


print("\nReorder Alerts:")

for item_name, details in inventory.items():
    stock = details["stock"]
    reorder_level = details["reorder_level"]

    if stock <= reorder_level:
        print(f"⚠ Reorder Alert: {item_name} — Only {stock} unit(s) left (reorder level: {reorder_level})")


## Final Comparison


print("\nFinal Inventory (After Orders):")
print(inventory)

print("\nBackup Inventory (Original):")
print(inventory_backup)

### Task 4: Daily Sales Log Analysis


print("\nDaily Revenue:")

daily_revenue = {}

##  Total revenue per day
for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date} → ₹{total:.2f}")

##  Best-selling day
best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nBest-selling day: {best_day} (₹{daily_revenue[best_day]:.2f})")


##  Most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print(f"\nMost ordered item: {most_ordered} ({item_count[most_ordered]} times)")


## Add new day


sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Daily Revenue:")

daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date} → ₹{total:.2f}")

best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nUpdated Best-selling day: {best_day} (₹{daily_revenue[best_day]:.2f})")



### Numbered Order List


print("\nAll Orders:")

all_orders = []

# collect all orders with date
for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

# print using enumerate
for i, (date, order) in enumerate(all_orders, start=1):
    items_str = ", ".join(order["items"])
    print(f"{i}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")


