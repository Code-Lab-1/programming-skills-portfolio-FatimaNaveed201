# Exercise 5: USB Shopper

#50p total 6p each
#how many can buy + how much money left

usb = 50
cost = 6
left = usb%cost
usbBought = int(usb/cost)
# print (penBought , left) 
print ("Total budget: " + str(usb))
print ("USB cost: " + str(cost))
print ("Total no. USB she's able to buy: " + str(usbBought))
print ("Money left after buying: " + str(left))
