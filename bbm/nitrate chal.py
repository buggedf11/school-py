nit = int(input("enter a nitrate number 1 to 50"))
if nit > 50:
    print("invalid number")
if nit > 10 :
    print("dose 3ml")
elif nit > 2.5:
    print("dose 2ml")
elif nit > 1 :
    print("dose 1ml")
else:
    print("dose 0.5ml")