class Stat:
    def __init__(self, nazev):
        self.nazev = nazev
        self.mesta = []

    def pridej_mesto(self, mesto):
        self.mesta.append(mesto)
    
    def info(self):
        pocet_mest = len(self.mesta)
        print(f'Stát {self.nazev} má {pocet_mest} měst.')

class Mesto:
    def __init__(self, nazev, stat):
        self.nazev = nazev
        self.stat = stat
        stat.pridej_mesto(self)
    
    def info(self):
        print(f'Město {self.nazev} leží ve státé {self.stat.nazev}.')

dansko = Stat('Dansko')
norsko = Stat('Norsko')

kodan = Mesto('Kodaň', dansko)
hovedstaden = Mesto('Hovedstaden', dansko)

oslo = Mesto('Oslo', norsko)

oslo.info()
kodan.info() 
dansko.info()