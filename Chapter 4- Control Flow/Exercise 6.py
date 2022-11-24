#Examination grading system

marks = int(input())
if marks >= 80:
  print ("A+ grade")
elif marks >= 70 and marks<= 79:
  print ("A grade")
elif marks >= 60 and marks<= 69:
  print ("B grade")
elif marks >= 40:
  print("Student has passed the examination")
else:
  print("Student has failed the examination")