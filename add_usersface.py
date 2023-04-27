import pyrebase
import bcrypt
import cv2
import os

# Initialize Firebase app

config = {
  # Add your Firebase config here
  "apiKey": "AIzaSyDprlN4oV51H2LAQMply1NYKfs56Nrw3rM",
  "authDomain": "nakulsdb.firebaseapp.com",
  "databaseURL": "https://nakulsdb-default-rtdb.firebaseio.com",
  "projectId": "nakulsdb",
  "storageBucket": "nakulsdb.appspot.com",
  "messagingSenderId": "916709408877",
  "appId": "1:916709408877:web:167b258e9ffc490954ff64",
  "measurementId": "G-GHGTG180R6"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Get user data
email = input("Enter email: ")
password = input("Enter password: ").encode('utf-8')

# Encrypt password
encrypted_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

# Open camera and wait for user to take photo
cap = cv2.VideoCapture(0)
cv2.namedWindow("Take a photo")
while True:
    ret, frame = cap.read()
    cv2.imshow("Take a photo", frame)
    key = cv2.waitKey(1)
    if key == ord(' '):  # Press spacebar to take photo
        photo_path = f"{email}.jpg"
        cv2.imwrite(photo_path, frame)
        break
cap.release()
cv2.destroyAllWindows()

# Load and store photo in Firebase Storage
storage = firebase.storage()
photo_url = storage.child(f"photos/{email}.jpg").put(photo_path)
photo_url = storage.child(f"photos/{email}.jpg").get_url(None)

# Store user data in Firebase Realtime Database
user_data = {
  "email": email,
  "password": encrypted_password,
  "photo_url": photo_url
}

db.child("users").push(user_data)

# Delete photo from disk
os.remove(photo_path)

print("User added successfully!")
