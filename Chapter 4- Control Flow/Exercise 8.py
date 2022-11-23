#temperature 

temperature = int(input())
if temperature <= 10:
    print("It's so cold today!")
elif temperature >= 10 and temperature <=30:
    print("The weather is so pleasant today!")
else:
    print("It's so hot today!")