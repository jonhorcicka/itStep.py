import math

def vypocet_obsahu(r):
  obsah = 3.14 * r**2
  return obsah

def vypocet_obvodu(r):
  obvod = 2 * 3.14 * r
  return obvod

# Zadaný poloměr
polomer = 7

# Výpočet obsahu a obvodu
obsah_kruhu = vypocet_obsahu(polomer)
obvod_kruhu = vypocet_obvodu(polomer)

# Výpis výsledků
print("Obsah kruhu o poloměru", polomer, "je:", obsah_kruhu)
print("Obvod kruhu o poloměru", polomer, "je:", obvod_kruhu)