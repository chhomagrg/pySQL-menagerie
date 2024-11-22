from connection import mydb

cursor = mydb.cursor()
cursor.execute("USE menagerie")
cursor.execute("SELECT name, birth, MONTH(birth) AS birth_month FROM pet")

print("+--------------------------------------+")
print(f"{'|  name':<11} |  {'birth':<10}|{'Month(Birth)':<9} |")
print("+-------------------------------------+")
for record in cursor.fetchall():
    print(f"| {record[0]:<10}| {record[1]} |        {record[2]:>4} |")
print("+--------------------------------------+")
cursor.close()
mydb.close()
