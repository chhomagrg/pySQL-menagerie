from connection import mydb

cursor = mydb.cursor()
cursor.execute("USE menagerie")

cursor.execute("SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner")

print("Number of pets each owner has:")
for record in cursor.fetchall():
    print(record)

cursor.close()
mydb.close()
