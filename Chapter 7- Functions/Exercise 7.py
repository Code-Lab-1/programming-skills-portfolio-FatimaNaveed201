#Finding exponents of the given number till 10

def exponent():
  num=int(input())
  for i in range (1,11):
    print(num, "**", i, "=", num**i)
exponent()