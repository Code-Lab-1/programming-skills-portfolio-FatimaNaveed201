# Exercise 6: Shrinking Guest List 

#Inviting people to dinner

guest_list = ["Harry Styles", "Louis Tomlinson", "Zayn Malik", "Liam Payne"]

invitation = f"Dear {guest_list[0].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

invitation = f"Dear {guest_list[1].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

invitation = f"Dear {guest_list[2].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

invitation = f"Dear {guest_list[3].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

unavailable = f"Sorry, {guest_list[2].title()} can't make it to dinner due to work."
print (unavailable)

#Zayn Malik is busy and cannot make it to dinner
#Lets invite Niall Horan instead!

print ("\nInviting Niall Horan instead and sending the invitations again!")

del(guest_list[2])
guest_list.insert(2, "Niall Horan")

#Printing the invitations again 

invitation = f"\nDear {guest_list[0].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

invitation = f"Dear {guest_list[1].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

invitation = f"Dear {guest_list[2].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

invitation = f"Dear {guest_list[3].title()}, I would like to invite you to dinner tonight. See you there!"
print (invitation)

#The table is not going to arrive in time for the dinner 
#Only two people can attend

print ("\nWe can only invite two people to dinner due to a smaller table.")

name = guest_list.pop()
print (f"\nSorry, {name.title()} there's no room at the table.")

name = guest_list.pop()
print (f"Sorry, {name.title()} there's no room at the table.")

#Only two people left. Inviting them again.

print ("\nInviting the two people left")

invitation = f"\nDear {guest_list[0].title()}, You are still invited to dinner. See you there!"
print (invitation)

invitation = f"Dear {guest_list[1].title()}, You are still invited to dinner. See you there!"
print (invitation)

#Emptying the list
del(guest_list[0])
del(guest_list[0])

#Checking if the list is empty or not

print (guest_list)