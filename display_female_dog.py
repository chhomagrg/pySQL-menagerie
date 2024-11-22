from connection import mydb

cursor = mydb.cursor()
cursor.execute("USE menagerie")

cursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")

for record in cursor.fetchall():
    print(record)

cursor.close()
mydb.close()
