# Exercise 5: Pets 

# Making the empty list.
pets = []

# Making individual dictionaries for different pets and storing each one in the list.

pet = {"animal":"cat",
"pet's name":"Leo",
"owner's name":"Fatima",
"pet's hobby":"playing with ball"}
pets.append(pet)

pet = {"animal":"dog",
"pet's name":"Lunala",
"owner's name":"Lily",
"pet's hobby":"going for walks"}
pets.append(pet)

pet = {"animal":"cow",
"pet's name":"Moomoo",
"owner's name":"Frank",
"pet's hobby":"being lazy all day"}
pets.append(pet)

pet = {"animal":"hamster",
"pet's name":"Hamtaro",
"owner's name":"Lenny",
"pet's hobby":"Eating sunflower seeds"}
pets.append(pet)

# Displaying each  pet's information.
for pet in pets:
    print("\nHere's the information I have about " + pet["pet's name"].title() + ": ")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))