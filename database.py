import mysql.connector
from mysql.connector import Error
from getpass import getpass
from PIL import Image
import io

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='nakuldb',
        user='root',
        password='1234'
    )
except Error as e:
    print(f"Error connecting to MySQL database: {e}")
    exit()

# Get user input
username = input("Enter username: ")
password = getpass("Enter password: ")
photo_path = input("Enter photo path: ")

# Open and read photo
try:
    with open(photo_path, 'rb') as f:
        photo_data = f.read()
    photo = Image.open(io.BytesIO(photo_data))
except FileNotFoundError:
    print("File not found.")
    exit()
except IOError:
    print("Invalid photo file.")
    exit()

# Insert user data into MySQL table
try:
    cursor = connection.cursor()
    sql_query = "INSERT INTO users (username, password, photo) VALUES (%s, %s, %s)"
    values = (username, password, photo_data)
    cursor.execute(sql_query, values)
    connection.commit()
    print("User data successfully inserted into MySQL database.")
except Error as e:
    print(f"Error inserting user data: {e}")
finally:
    cursor.close()
    connection.close()
