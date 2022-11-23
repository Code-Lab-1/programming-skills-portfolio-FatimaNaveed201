#Finding the largest number the user inputs

def maxnumber():
  a=input()
  b=input()
  c=input()

  if a>b and a>c:
    print("The largest number is: " + a)
  elif b>a and b>c:
    print("The largest number is " + b)
  else:
    print("The largest number is " + c)
maxnumber()