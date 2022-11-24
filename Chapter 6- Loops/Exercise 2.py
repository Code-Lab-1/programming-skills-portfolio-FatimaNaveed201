# Exercise 2: Movie Ticket

task = "How old are you?"
task += "\nEnter 'quit' when you are done. \n"

while True:
    age = input(task)
    if age == 'quit':
        break
    
    age = int(age)

    if age < 3:
        print ("Your ticket is free!!")
    elif age < 13:
        print("Your ticket costs $10. ")
    else: 
        print("Your ticket costs $15. ")
