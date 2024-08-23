
cisla = [-98, 23, 27, 91, -46, -26, -69, -53, -62, -93, 17, 50, -65, 18, -38, -4, 75, -79, -98, -56, -57, 89]

pocet_zapornych = 0
pocet_kladnych = 0

for cislo in cisla:
    if cislo < 0:
        pocet_zapornych += 1
    elif cislo > 1:
        pocet_kladnych += 1

print("Počet - čísel:", pocet_zapornych)
print("Počet + čísel:", pocet_kladnych)
