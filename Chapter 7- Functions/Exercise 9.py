#Displaying the table of the number that the user inputs

def table():
  num=int(input())
  for i in range (1,11):
    print(num, "x", i, "=", num*i)

table()