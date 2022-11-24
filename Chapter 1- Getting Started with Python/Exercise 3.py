## Exercise 3: Print date and Time

import datetime
now = datetime.datetime.now()
print ("The Current date and time is: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))