import psycopg2
mydb = psycopg2.connect(user="lidor",
                                password="lidor1408",
                                host="localhost",
                                port="5432",
                                database="lidor")

mycursor = mydb.cursor()

sql = "INSERT INTO EMPLOYEE (fname, lname, id) VALUES (%s,%s, %s)"
val = ("lee", "WAY 23",4)
mycursor.execute(sql, val)
count = mycursor.rowcount
postgreSQL_select_Query = "select * from EMPLOYEE"
mycursor.execute(postgreSQL_select_Query)
print("Selecting rows from EMPLOYEE table using cursor.fetchall")
EMPLOYEE_records = mycursor.fetchall() 
print(" each row and it's columns values")

for row in EMPLOYEE_records:
    disx=row[0]
    print("Id = ", row[2], )
    print("fname = ", row[0])
    print("lanme = ", row[1], "\n")

mydb.commit()

print(mycursor.rowcount, "record inserted.")