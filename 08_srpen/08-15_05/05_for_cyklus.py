data = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]

for vyska in data:
    if vyska < 3000:
        print(f"{vyska} m je nízká výška")
    elif vyska < 6000:
        print(f"{vyska} m je střední výška")
    else:
        print(f"{vyska} m je vysoká výška")