#multiplying all items in a dictionary

dictionary = {"value1":3, "value2":10, "value3":1, "value4":5}
answer = 1
for key in dictionary:
    answer=answer * dictionary[key]

print("The sum of all the values in the dictionary is : ")
print(answer)