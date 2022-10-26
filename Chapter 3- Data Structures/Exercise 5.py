# Exercise 5: Change Guest List

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