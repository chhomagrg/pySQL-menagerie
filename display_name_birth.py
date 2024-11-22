from connection import mydb

cursor = mydb.cursor()
cursor.execute("USE menagerie")

cursor.execute("SELECT name, birth FROM pet")

for record in cursor.fetchall():
    print(record)

cursor.close()
mydb.close()

