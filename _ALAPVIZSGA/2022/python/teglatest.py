def Alakzat():
    szam1 = int(input("Kérem az A oldal méretét"))
    szam2 = int(input("Kérem a B oldal méretét"))
    kerulet = 2*szam1+2*szam2
    terulet = szam1*szam2
    print(f"Kerülete: {kerulet}, Területe: {terulet}")
    uj = input("Szeretne ujabb szamitast i/n")
    while uj != "i" and uj != "n":
        print("Csak i-t és h-t fogadok el")
        uj = input("Szeretne ujabb szamitast i/n")
    while uj == "i":
        szam1 = int(input("Kérem az A oldal méretét"))
        szam2 = int(input("Kérem a B oldal méretét"))
        print(f"Kerülete: {kerulet}, Területe: {terulet}")
        uj = input("Szeretne ujabb szamitast i/n")

        if uj == "n":
            print()

Alakzat()
