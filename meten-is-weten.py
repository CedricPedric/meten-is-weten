a = input("Voer hier getal A in: ")
b = input("Voer hier getal B in: ")

if a>b:
    Max = a
    Min = b 
    print("a is het grootste getal " + str(Max))
    print('Het minimum is: ' + str(Min))

elif a<b:
    Min = a
    Max = b
    print("a is het kleinste getal: " + str(Min))
    print("Het maximum is: " + str(Min))

else: 
    print("a en b zijn even groot")
