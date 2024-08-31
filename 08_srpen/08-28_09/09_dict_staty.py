staty = {
    'CZ': 'Česko',
    'SK': 'Slovensko',
    'PL': 'Polsko',
    'DE': 'Německo',
    'AT': 'Rakousko',
}

staty['HU'] = 'Maďarsko'

staty_delka = {}

for key, stat in staty.items():
    staty_delka[key] = len(stat)

    print()
    print(key, stat)
    print(key, staty_delka[key])
    print()
    

