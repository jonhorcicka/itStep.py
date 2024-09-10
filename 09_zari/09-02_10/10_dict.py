ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}
# a)
ceny_potravin['mléko'] = 25
print(ceny_potravin)

# b)
nejlevnejsi_produkt = min(ceny_potravin, key=ceny_potravin.get)
nejlevnejsi_cena = ceny_potravin[nejlevnejsi_produkt]
print("Nejlevnější je:", nejlevnejsi_produkt, nejlevnejsi_cena, "kč")

# c)
celkova_cena = 4 * ceny_potravin['jablko'] + ceny_potravin['máslo'] + 2 * ceny_potravin['sýr']
print("Celková cena je:", celkova_cena,"kč")
