#Reversing a list using function

def reversing():
  a=int(input())
  b=int(input())
  c=int(input())
  d=int(input())
  e=int(input())

  num = [a, b, c, d, e]
  print("\nThe original sequence: ")
  print(num)
  
  num.reverse()
  print("\nThe reversed sequence: ")
  print(num)

reversing()