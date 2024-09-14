mesta_cr = {
    "Praha": 1300000,
    "Brno": 380000,
    "Ostrava": 290000,
    "Plzeň": 170000,
    "Liberec": 100000,
    "Olomouc": 100000,
    "Ústí nad Labem": 92000,
    "Hradec Králové": 93000,
    "České Budějovice": 94000,
    "Pardubice": 90000
}

def info(nazev_mesta):
    try:
        pocet_obyvatel = mesta_cr[nazev_mesta]
        print(f"{nazev_mesta}: {pocet_obyvatel} obyvatel")
    except KeyError:
        print(f"Neznámé město: {nazev_mesta}")

print('')
info('Praha')
print('')
info('Pardubice')
print('')
info('New York')
print('')
info('Amsterdam')
print('')