eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]

celkovy_pocet_obyvatel = 0
mesto_s_nejvice_obyvateli = ""
max_pocet_obyvatel = 0
mesto_s_nejmene_obyvateli = ""
min_pocet_obyvatel = float('inf') # dal jsem 0, a to mi mesto a min_oby neukazalo, tak jsem zjistovat duvod proč, a zjistil, že je potřeba float('int') (123.23435) - poprosím o vysvětlení proč je potřeba float('int') misto 0, a co je ('inf') a proč nelze bez toho?

for mesto in eu_cities:
    nazev_mesta, pocet_obyvatel, rozloha = mesto
    celkovy_pocet_obyvatel += pocet_obyvatel
    
    if pocet_obyvatel > max_pocet_obyvatel:
        max_pocet_obyvatel = pocet_obyvatel
        mesto_s_nejvice_obyvateli = nazev_mesta

    if pocet_obyvatel < min_pocet_obyvatel:
        min_pocet_obyvatel = pocet_obyvatel
        mesto_s_nejmene_obyvateli = nazev_mesta

print("Celkový počet:", celkovy_pocet_obyvatel)
print()
print("Město s max obyvatel:", mesto_s_nejvice_obyvateli,'\n' "max obyvatel:", max_pocet_obyvatel)
print()
print("Město s min obyvatel:", mesto_s_nejmene_obyvateli,'\n' "min obyvatel:", min_pocet_obyvatel)

