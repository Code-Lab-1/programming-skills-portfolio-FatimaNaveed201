#Combining two dictionaries

dictionary1 = {"a":10, "b":20, "c":30, "d":40}
dictionary2 = {"e":50, "f":60, "g":70, "h":80}

dictionary = dictionary1.copy()
dictionary.update(dictionary2)
print(dictionary)