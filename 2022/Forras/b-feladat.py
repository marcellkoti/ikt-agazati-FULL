# teglalap kerulet terulet
folytatom = True
while folytatom:
    a = int(input("a: "))
    b = int(input("b: "))
    k = 2 * (a + b)
    t = a * b
    print(f"Kerület: {k}")
    print(f"Terület: {t}")
    tovabb = input("Szeretnél újabb téglalapot számolni? (i/n): ")  
    if tovabb!="i":
        folytatom = False
print("Viszlát!")