# Exercise 4: Rivers 

Rivers = {"The Indus River":"Pakistan",
"The Mekong River":"China",
"The Amur River":"Russia",
"The Zambezi River":"Zambia"}

for river, country in Rivers.items():
    print(river.title() + " runs through " + country.title() + ". ")

print("\nThe rivers included in this dictionary are as follows: ")
for river in Rivers.keys():
    print (" - " + river.title())

print("\nThe countries included in this dictionary are as follows: ")
for country in Rivers.values():
    print(" - " + country.title())