# Exercise 3: Glossary 2 

Glossary = {"Comment":"A python comment is a line of text that appears in a program but is not executed. Comments are used to explain the code.",
"Escape character":"It is used to insert the special characters in a string. It is a backslash \ followed by the special character.", 
"print()":"The print function is used to print the string or value.",
"Boolean":"Booleans represnt one of the two values i.e., True and False.",
"Lists":"lists in python are used to store multiple values and items in a single variable. A list is an ordered and changeable collection of data.",
"String":"A python string is a sequence of characters. It is an immutable data sequence.",
"input()":"The input function in python is used to take the user input.",
"Concatenation":"Concatenation in python means joining two or more strings together to form a single string.",
"Dictionary":"A dictionary in python is a collection of key-value pairs.",
"Iteration":"The repetitive execution of the same code over and over again is called iteration."}

for word, definition in Glossary.items():
    print("\n" + word.title() + ": " + definition)