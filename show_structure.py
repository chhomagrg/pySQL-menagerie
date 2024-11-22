from connection import mydb

cursor = mydb.cursor()

cursor.execute("USE menagerie")
cursor.execute("DESCRIBE pet")

for column in cursor.fetchall():
    print(column)