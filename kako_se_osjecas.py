x = input("Kako se osjećaš?: ")
mood = x.lower()
if mood == "sretno":
    print("Drago mi je da si sretan!")
elif mood == "nervozno":
    print("Popij čaj i duboko diši.")
elif mood == "tužno":
    print("Poslije kiše dolazi sunce.")
elif mood == "uzbuđeno":
    print("Ovo je veliki dan!")
elif mood == "opušteno":
    print("Uživaj u danu!")
else:
    print("Ne razumijem.")
