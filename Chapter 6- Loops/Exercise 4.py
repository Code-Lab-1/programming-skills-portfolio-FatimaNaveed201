# Exercise 4: Deli

sandwich_orders = ["chicken sandwich", "cheese sandwich", "beef sandwich", "pepperoni sandwich", "vegetable sandwich", "egg sandwich"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am currently making your " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("\n")

for sandwich in finished_sandwiches:
    print("I have finished making your " + sandwich + ".")