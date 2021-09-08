vraag1 = input("Heeft u meer dan 4 jaar praktijkervaring met dieren-dressuur? yes or no: ")
vraag2 = input("Heeft u meer dan 5 jaar ervaring met jongleren? yes or no: ")
vraag3 = input("Heeft u meer dan 3 jaar praktijkervaring met acrobatiek? yes or no: ")
vraag4 = input("Bent u in bezit van een Diploma MBO-4 ondernemen? yes or no: ")
vraag5 = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? yes or no:")
vraag6 = input("Ben u in bezit van een hoge hoed? yes or no:")
vraag7 = input("Bent u een man? yes or no: ")
vraag8 = int(input("Zoja hoe breed is u snor in cm (bent u een vrouw type: 0):  "))
vraag9 = input("Bent u een vrouw? yes or no: ")
vraag10 = input("Zoja is u haar rood en krullig? yes or no: ")
vraag11 = int(input("Zoja hoelang draag u uw haar in cm?(bent u een man type: 0): "))
vraag12 = int(input("Hoelang bent u in cm?: "))
vraag13 = int(input("Hoe zwaar weegt u in hele kg?: "))
vraag14 = input("Heeft u het certificaat “Overleven met gevaarlijk personeel”? yes or no: ")
vraag15 = input("Houd u van uw vrouw of man? yes or no: ")
vraag16 = input("Houd u van donuts? yes or no: ")
vraag17 = input("Wie is uw favoriete K3 lid?: ")
vraag18 = input("Wat vond u van deze solicitatie-test?: ")


if vraag1 == ("yes" or vraag2 == "yes" or vraag3 == "yes" and vraag4 == "yes" and vraag5 == "yes"
and vraag6 == "yes" and vraag7 == "yes" and vraag8 > 10 or vraag9 == "yes" and vraag10 == "yes" and vraag11 > 20
and vraag12 > 150 and vraag13 > 90 and vraag14 == "yes"):
    print("je bent aangenomen!")  
else:
    print("je bent niet aangenomen!") 
