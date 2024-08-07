cesta = '08_srpen/7-8_02/user.txt'

jmeno = input("Zadej své jméno: ")
vek = input("Zadej svůj věk: ")

with open(cesta, "w") as file:
    file.write(f"Jméno: {jmeno}\nVěk: {vek}")


