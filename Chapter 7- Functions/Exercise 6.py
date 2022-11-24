#Taking user input and separating odd and even numbers in different lists.
def oddeven():
  a=int(input())
  b=int(input())
  c=int(input())
  d=int(input())
  e=int(input())
  nums=[a,b,c,d,e]
  evenlist=[]
  oddlist=[]

  for i in nums:
    if i%2==0:
      evenlist.append(i)
    else:
      oddlist.append(i)
  print("The even list: ", evenlist)
  print("The odd list: ", oddlist)
        

oddeven()