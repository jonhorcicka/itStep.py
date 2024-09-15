class Planeta:
    def __init__(self, poradi, nazev):
        self.poradi = poradi
        self.nazev = nazev
    
    def info(self):
        print(f"Toto je {self.nazev} a je {self.poradi}. planeta od Slunce.")

merkur = Planeta(1, "Merkur")
zeme = Planeta(3, "Země")
saturn = Planeta(6, "Saturn")

merkur.info()
zeme.info()
saturn.info()
