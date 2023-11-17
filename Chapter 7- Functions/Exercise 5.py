# Exercise 5: Cities

def describe_cities(city, country="United States of America"):
    message = "The city of " + city.title() + " is in " + country.title() + ". "
    print(message)


describe_cities("Houston")
describe_cities("New York")
describe_cities("Lahore", "Pakistan")