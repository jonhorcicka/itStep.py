import sqlite3

cesta = '11_listopad/11-04_25/chinook.db'
conn = sqlite3.connect(cesta)
cursor = conn.cursor()

#1)
cursor.execute('SELECT * FROM tracks ORDER BY Milliseconds DESC LIMIT 3')
longest_tracks = cursor.fetchall()
print("3 nejdelší skladby:")
for track in longest_tracks:
    print(track)

#2)
cursor.execute('UPDATE artists SET Name = "Moje kapela" WHERE Name = "Test"')

conn.commit()
conn.close()
