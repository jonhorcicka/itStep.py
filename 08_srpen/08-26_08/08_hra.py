import random

cislo = random.randint(1, 10)

while True:
    uzivatel_cisla = int(input('Hádej číslo od 1 do 10: '))

    if uzivatel_cisla == cislo:
        print(f"Výborně! Uhádl jsi číslo {cislo}.")
        break