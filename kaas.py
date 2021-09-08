isKaas1 = input("Is de kaas geel? ja of nee: ")
if isKaas1 == "ja":
    isKaas2 = input("Zitten er gaten in? ja of nee: ")
    if isKaas2 =="ja":
        isKaas3 = input("Is de kaas belachelijk duur? ja of nee: ")
        if isKaas3 == "ja":
            print("Emmenthalter")
        elif isKaas3 == "nee":
            print("Leerdammer")
    elif isKaas2 == "nee":
        isKaas3 = input("Is de kaas zo hard als steen?: ")
        if isKaas3 == "ja":
            print("Pamnigiano Reggiano")
        elif isKaas3 == "nee":
            print("Goudse kaas")
        
elif isKaas1 == "nee":
    isKaas2 = input("Heeft de kaas blauwschimmels? ja of nee: ")
    if isKaas2 =="ja":
        isKaas3 = input("Heef de kaas een korst?: ")
        if isKaas3 == "ja":
            print("Blue de Rochbaron")
        elif isKaas3 == "nee":
            print("Foumme d'Ambert")
    elif isKaas2 == "nee":
        isKaas3 = input("Heeft de kaas een korst?: ")
        if isKaas3 == "ja":
            print("Camebert")
        elif isKaas3 == "nee":
            print("Mozzarella")

