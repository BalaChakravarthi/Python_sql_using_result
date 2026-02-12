import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4447",
        database="resultdb"
    )

    cursor = mydb.cursor(buffered=True)   # IMPORTANT

    roll = input("Enter Student Roll Number: ")

    query = "SELECT * FROM results WHERE roll_no = %s"
    cursor.execute(query, (roll,))

    result = cursor.fetchone()

    if result:
        print("\n----- STUDENT RESULT -----")
        print("ID:", result[0])
        print("Name:", result[1])
        print("Roll No:", result[2])
        print("Subject 1:", result[3])
        print("Subject 2:", result[4])
        print("Subject 3:", result[5])
        print("Subject 4:", result[6])
        print("Subject 5:", result[7])
        print("Subject 6:", result[8])
        print("Total:", result[9])
        print("Percentage:", round(result[10], 2), "%")
    else:
        print("No student found.")

except mysql.connector.Error as err:
    print("Database Error:", err)

finally:
    try:
        if cursor:
            cursor.close()
        if mydb:
            mydb.close()
        print("\nConnection Closed Successfully.")
    except:
        pass
