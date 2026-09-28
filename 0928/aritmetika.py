'''aoldal=float(input("Add meg a négyzet oldalának hosszát: "))
K=4*aoldal
T=aoldal*aoldal

print("A négyzet kerülete ", K, " cm")
print("A négyzet területe: ", T, " cm2")'''

aoldal=float(input("Add meg a téglatest oldalainak hosszát: "))
boldal=float(input("Add meg a téglatest oldalainak hosszát: "))
coldal=float(input("Add meg a téglatest oldalainak hosszát: "))

F=2*(aoldal*boldal+boldal*coldal+coldal*aoldal)
V=aoldal*boldal*coldal
 
print("A téglatest felszíne: ", F, " cm2")
print("A téglatest térfogata: ", V, " cm3")