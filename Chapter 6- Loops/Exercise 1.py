# Exercise 1: Pizza Toppings

task = "\n Which toppings would you like on your pizza?"
task += "\n Type 'quit' when you are done.  \n "

while True:
    topping = input(task)
    if topping != 'quit':
        print("\nOkay I will add " + topping + " to your pizza.")
    else:
        break