from connection import mydb

cursor = mydb.cursor()

cursor.execute("DROP DATABASE IF EXISTS menagerie")
print("Database menagerie has been dropped if it existed.")

mydb.close()


