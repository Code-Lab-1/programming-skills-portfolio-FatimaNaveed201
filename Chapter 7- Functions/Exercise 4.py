#Exercise 4:  Large Shirts

def make_shirt(size = "large", message = "I love python!"):
    print("\nYou ordered a " + size + " shirt which will say: '" + message + "'")
    
make_shirt()
make_shirt(size = "medium")
make_shirt("extra small", "I'm tired")