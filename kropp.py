def spelplan(): #funktion för att skriva ut spelplanen
    for i in range(0,3):
        temp = ""
        for j in range(0,3):
            if(j > 0):
                temp += "|"
            temp += plan[i][j]
        print(temp)
        if i < 2:
            print('-----')


rad0 = [" ", " ", " "]
rad1 = ["o", " ", " "]
rad2 = [" ", " ", "x"]
plan = [rad0, rad1, rad2]
spelplan()
tur = "x"

while(True):
    print("Det är spelare " + tur + ":s tur.")
    ok = True
    while (ok):
        r = int(input("Välj rad: ")) - 1
        while(r>2):
            r = int(input("Välj en rad mellan 1 och 3: ")) - 1
        k = int(input("Välj kolumn: ")) - 1
        while(k>2):
            k = int(input("Välj en kolumn mellan 1 och 3: ")) -1

        if (plan[r][k] != " "):
            print("Den platsen är upptagen, försök igen spelare " + tur + "!")
        else:
            ok = False

    plan[r][k] = tur
    spelplan()

    if(tur == "x"):
        tur = "o"
    else:
        tur = "x"
