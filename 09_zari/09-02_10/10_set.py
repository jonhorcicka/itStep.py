friends_set1 = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"}
friends_set2 = {"Charlie", "Eve", "Bob", "Frank", "Mallory", "Oscar", "Peggy", "Trent", "Victor", "Walter"}

print("")

celkovy_pocet_lidi = len(friends_set1 | friends_set2)
print("Celkový počet lidí:",celkovy_pocet_lidi)

print("")

spolecni_pratele = friends_set1 & friends_set2
print("Společní přátelé:",spolecni_pratele)

print("")
