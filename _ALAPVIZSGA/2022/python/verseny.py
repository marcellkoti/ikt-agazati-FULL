class Eredmeny:
    def __init__(self,nev,szam) :
        self.nev = nev
        self.szam = int(szam)
        
    def __str__(self):
        return f"{self.nev}, {self.szam}"

def Beolvasas(fajlnev):
    versenyek = []
    try:
        with open(fajlnev,"rt",encoding="utf-8") as file:
            for sor in file:
                if sor.strip():
                    adat = sor.strip().split(";")
                    #print(f"Beolvasott adatok: {adat}")
                    if len(adat) == 2:
                        try:
                            nev,szam = adat
                            versenyek.append(Eredmeny(nev,szam))
                        except ValueError:
                            print("Hibás adatsor")
                    else:
                        print("Hibás adatsor")
    except FileNotFoundError:
        print("A fájl nem lett megadva")
        return []
    return versenyek

versenyek = Beolvasas("eredmeny.txt")
for verseny in versenyek:
    print(f"Név: {verseny.nev}, Eredménye: {verseny.szam}")


tjut = int(input("Mennyi a továbbjutáshoz szükséges pont? "))
talalat = [v for v in versenyek if v.szam >= tjut]
if talalat:
    print(f"Az adott versenyen {len(versenyek)} résztvevő volt és ebből {len(talalat)} a továbbjutók száma")



