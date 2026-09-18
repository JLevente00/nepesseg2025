import msvcrt

adatok = []

with open("lakossag_2025.csv", "r", encoding="utf-8") as forras:
    fejlec = forras.readline()
    for sor in forras:
        if sor.strip():
            adat = sor.strip().split(";")
            adatok.append(
                {
                    "megyekod": adat[0],
                    "telepules": adat[1],
                    "tipus": adat[2],
                    "ferfi": int(adat[3].replace(" ", "")),
                    "no": int(adat[4].replace(" ", "")),
                }
            )

def menu_1():
            print(" Adja meg a megyekódot: ")
            megyekod = "" 
            megyekkodok = ["BAC","BAR","BEK","BOR","BUD","CSO","FEJ","GYO","HAJ","HEV","KOM","NOG","PES","SOM","SZA","SZO","TOL","VAS","VES","ZAL",]
            for i in range(3):
                megyekod_egy_eleme = msvcrt.getch().decode("utf-8")
                megyekod += megyekod_egy_eleme.upper()
            if megyekod in megyekkodok:
                return megyekod
            else:
                print("A megadott megyekód nem szerepel az adatbázisban.")
                print("Vissza szeretne térni a menübe vagy folyattod a keresést \n [1]-Menü \n [2]-Keresés folyatatása")
                visszateres = msvcrt.getch().decode("utf-8")
            if visszateres == "1":
                return menu()  
            elif visszateres == "2":
                return menu_1()  

def menu_2():
            print("[A] - Község")
            print("[B] - Város")
            print("[C] - Nagyközség")
            print("[D] - Fővárosi kerület")
            print("[E] - Vármegyeszékhely")
            print("[F] - Vármegyei jogú város")
            masodikmenu_betukod = msvcrt.getch().decode("utf-8")
            if masodikmenu_betukod.upper() == "A":
                print("Község")
                return "Község"
            elif masodikmenu_betukod.upper() == "B":
                print("Város")
                return "Város"
            elif masodikmenu_betukod.upper() == "C":
                print("Nagyközség")
                return "Nagyközség"
            elif masodikmenu_betukod.upper() == "D":
                print("Fővárosi kerület")
                return "Fővárosi kerület"
            elif masodikmenu_betukod.upper() == "E":
                print("Vármegyeszékhely")
                return "Vármegyeszékhely"
            elif masodikmenu_betukod.upper() == "F":
                print("Vármegyei jogú város")
                return "Vármegyei jogú város"

def menu():
    print("----------------------")
    print("Üdvözöljük válaszon a lehetőségek közül!")
    print("[1] Megye adatai")
    print("[2] Település típusai")
    print("[3] Opció \n")
    print("[X] kilépés a programból")
    print("----------------------")
    menuvalaszto = msvcrt.getch().decode("utf-8")
    if menuvalaszto == "1":
        return menu_1()  
    elif menuvalaszto == "2":
        return menu_2()  
    elif menuvalaszto == "3":
        print("Fejlesztés alatt...")
        print("Vissza szeretne térni a menübe \n [1]-Igen \n [2]-Nem")
        fejlesztes_alatt_visszateres = msvcrt.getch().decode("utf-8")
        if fejlesztes_alatt_visszateres == "1":
            return menu()  
        elif fejlesztes_alatt_visszateres == "2":
            print("Kilépés a programból")
    elif menuvalaszto.upper() == "X":
        print("Program vége.")
    else:
        print("\n\n Rossz bilentűlenyomás történt, próbálozzon újra \n")
        return menu()

valasz = menu() 
 
telepulesek_szama = 0

for a in adatok:
    if a["megyekod"] == valasz:
        telepulesek_szama += 1

osszes_lakossag = 0

for a in adatok:
    if a["megyekod"] == valasz:
        a["ferfi"] = int(a["ferfi"])
        a["no"] = int(a["no"])
        osszes_lakossag += a["ferfi"] + a["no"]
        
osszes_varosilakossag = 0   

varosi_tipusok = ["város","vármegyei jogú város","fővárosi kerület","vármegyeszékhely",]

for a in adatok:
    if a["megyekod"] == valasz and a["tipus"] in varosi_tipusok:
        osszes_varosilakossag += int(a["ferfi"]) + int(a["no"])
if valasz in ["BAC","BAR","BEK","BOR","BUD","CSO","FEJ","GYO","HAJ","HEV","KOM","NOG","PES","SOM","SZA","SZO","TOL","VAS","VES","ZAL",]:
    print(f"A megadott megyekódhoz tartozó városi lakosság összege: {osszes_varosilakossag}")
    print(f"A megadott megyekódhoz tartozó települések száma: {telepulesek_szama}")
    print(f"A megadott megyekódhoz tartozó lakosság összege: {osszes_lakossag}")

varosnevek = []


if valasz == "Fővárosi kerület":
     for a in adatok:
          if a["tipus"] == "fővárosi kerület":
               varosnevek.append(a["telepules"])
               

