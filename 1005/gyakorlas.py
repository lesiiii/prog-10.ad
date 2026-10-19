'''ido=int(input("Az idő másodpercben: "))

ora=ido//3600
print("Óra: ", ora)

perc=(ido%3600)//60
print("Perc: ", perc)

masodperc=(ido%3600)%60
print("Másodperc: ", masodperc)'''
'idős feladat'

megtett_ut=float(input("Megtett út (km): "))
uzemanyag=float(input("Tankolt mennyiség (l): "))
atlagfogyasztas=uzemanyag/megtett_ut*100
print("Átlagfogyaztás: ", round(atlagfogyasztas, 1), "l/100km")