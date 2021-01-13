
card = input("Put in your credit card number ")
type = int(card[0])

if type == 3:
    print(" you have an american express card")
elif type == 4:
    print("you have a visa card")
elif type == 5:
    print("you have a mastercard")
elif type == 6:
    print("you have a discover card")
else:
    print("this is not a supported card")