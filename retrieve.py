import mysql.connector
from PIL import Image

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="nakuldb"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define the SELECT statement
sql = "SELECT username, password, photo FROM users"

# Execute the SELECT statement
mycursor.execute(sql)

# Fetch all the rows
rows = mycursor.fetchall()

# Loop through the rows
for row in rows:
    username = row[0]
    password = row[1]
    photo_data = row[2]
    
    # Save the photo to a file
    with open(f"{username}.jpg", "wb") as file:
        file.write(photo_data)
    
    # Display the photo using Pillow
    img = Image.open(f"{username}.jpg")
    img.show()

# Close the database connection
print(username)
print(password)
mydb.close()
