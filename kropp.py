def spelplan(): #funktion för att skriva ut spelplanen
    for i in range(0,3):
        temp = ""
        for j in range(0,3):
            if(j > 0):
                temp += "|"
            temp += plan[i][j]
        print(temp)


rad0 = [" ", " ", " "]
rad1 = ["o", " ", " "]
rad2 = [" ", " ", "x"]
plan = [rad0, rad1, rad2]
spelplan()
tur = "x"

while(True):
    print("Det är spelare " + tur + " tur.")
    r = int(input("Välj rad: "))
    k = int(input("Välj kolumn: "))
    plan[r-1][k-1] = tur
    spelplan()

    if(tur == "x"):
        tur = "o"
    else:
        tur = "x"
