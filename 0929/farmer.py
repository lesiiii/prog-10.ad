'''X=(3600/0.75)/1.2
print("A farmer eredeti ára: ", X, "Ft")

toltet=750-(750*0.12)
print(toltet, "g")'''

'''meret=int(input("Kérem adja meg a konzerv sulyát grammokban: "))
toltet=meret-(meret*0.12)
print(toltet, "g")'''

'''kereset=int(input("Kérem adja meg a keresetét: "))
netto=kereset*0.665
print("A nettó keresete: ", netto, "Ft")'''

import math

r=int(input("Kérem adja meg a kör sugarát: "))

K=2*math.pi*r
T=math.pi*r**2
print("A kör kerülete: ", K, " cm")
print("A kör területe: ", T, " cm2")
