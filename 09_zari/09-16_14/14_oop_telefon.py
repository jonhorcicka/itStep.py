class MobilPhone:
    def __init__(self, brand, model, software, uloziste, barva):
        self.brand = brand
        self.model = model
        self.software = software
        self.uloziste = uloziste
        self.barva = barva

    def zavolat(self, cislo):
        print(f'Volám na číslo {cislo}')

    def poslat_zpravu(self, prijemce, zprava):
        print(f'Posílám zprávu {zprava} na číslo {prijemce}')

phone1 = MobilPhone('Apple', 'iPhone 13 mini', 'iOS', '256GB', 'Červená')

phone2 = MobilPhone('Samsung', 'Galaxy S23', 'Android', '256GB', 'Zelená')

phone3 = MobilPhone('Google', 'Pixel 9 Pro', 'Android', '128GB', 'Šedá')

phone1.zavolat("123098567")
phone1.poslat_zpravu("999888777", "Ahoj, jak se máš?")

phone2.zavolat("777777777")
phone2.poslat_zpravu("121212121", "Mám hlad, zajdeme na jídlo?")

phone3.zavolat("222222222")
phone3.poslat_zpravu("666777222","Mám skvělé zprávy.")
