# Exercise 5: No Pastrami

sandwich_orders = [
    "chicken sandwich", "pastrami", "cheese sandwich", "beef sandwich", "pastrami", "pepperoni sandwich", "vegetable sandwich", "egg sandwich", "pastrami"]
finished_sandwiches = []

print("Sorry but we've run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I am currently making your " + current_sandwich + ".")
    finished_sandwiches.append(current_sandwich)

print("\n")

for sandwich in finished_sandwiches:
    print("I have finished making your " + sandwich + ".")