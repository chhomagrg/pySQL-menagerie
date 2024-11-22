from connection import mydb

cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")

# Display databases
for db in cursor:
    print(db[0])

cursor.close()
mydb.close()
