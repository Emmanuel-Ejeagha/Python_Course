import pymysql

try:
    con = pymysql.connect(
        host='localhost',
        user='backend-developer',
        password='StrongPassword123!',
        port=3306  # Specify the port if it's different from the default
    )
    print("Connected to MySQL database successfully!")
    mycursor = con.cursor()
    # Continue with your database operations here
except pymysql.Error as e:
    print(f"Error connecting to MySQL database: {e}")
finally:
    if con:
        con.close()  # Close the connection when done

