cart = (2, 3, 4, 8)

cart = int(raw_input("Please enter your cart No.: "))
for val in cart:
    if val > 4:
        print ("You are next!")
    break
else:
    print ("Try Again!")