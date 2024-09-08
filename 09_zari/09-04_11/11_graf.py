import matplotlib.pyplot as plt

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzeň': 185_599,
}

mesto = list(data.keys())
populace = list(data.values())

plt.bar(mesto, populace, color='olive')

plt.xlabel('Město')
plt.ylabel('Populace')

plt.title('Počet obyvatel ve vybraných městech ČR')

plt.show()