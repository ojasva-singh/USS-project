import pyrebase
import urllib.request
import cv2
import numpy as np



# Firebase config key
firebaseConfig = {
    "apiKey": "AIzaSyDprlN4oV51H2LAQMply1NYKfs56Nrw3rM",
    "authDomain": "nakulsdb.firebaseapp.com",
    "databaseURL": "https://nakulsdb-default-rtdb.firebaseio.com",
    "projectId": "nakulsdb",
    "storageBucket": "nakulsdb.appspot.com",
    "messagingSenderId": "916709408877",
    "appId": "1:916709408877:web:167b258e9ffc490954ff64",
    "measurementId": "G-GHGTG180R6"
}

# Firebase Authentication
firebase = pyrebase .initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()


# Load user's photo from Firebase
def load_photo_url_from_firebase(email):
    all_users = db.get().val()["users"]
    # print(all_users.keys())
    for item in all_users.items():
        # print(item[1]["email"])
        i_val = item[1]["email"]
        if (i_val == email):
            # uid = item.key()
            photo_url = item[1]["photo_url"]

            if (photo_url == None):
                print("No photo found for this user")
                return None
            else:
                return photo_url


email = input("Enter your email address: ")

# Load user's photo from Firebase
stored_photo = load_photo_url_from_firebase(email)
print(stored_photo)


# Set a flag to check if authentication is successful or not
flag = False

# Load the reference image from a stored photo

with urllib.request.urlopen(stored_photo) as url:
    img_array = np.asarray(bytearray(url.read()), dtype=np.uint8)
    reference_image = cv2.imdecode(img_array, -1)


# reference_image = cv2.imread("C:/Users/My Dell/Pictures/Camera Roll/264.jpg")

# Load the face detection model
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Convert the reference image to grayscale
reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the reference image
reference_faces = face_detector.detectMultiScale(reference_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Extract the first face found in the reference image
if len(reference_faces) > 0:
    (ref_x, ref_y, ref_w, ref_h) = reference_faces[0]
    reference_face = reference_gray[ref_y:ref_y+ref_h, ref_x:ref_x+ref_w]
    reference_face = cv2.resize(reference_face, (100, 100))
else:
    print('No face found in the reference image!')
    exit()

# Initialize the video capture device
cap = cv2.VideoCapture(0)
counter=0


while True and counter<1000:
    # Read a frame from the video capture device
    print(counter)
    counter=counter+1
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through the detected faces and compare them with the reference face
    for (x, y, w, h) in faces:
        # Extract the current face from the grayscale frame
        print(x, y, w, h)
        current_face = gray[y:y+h, x:x+w]
        current_face = cv2.resize(current_face, (100, 100))

        # Compute the absolute difference between the current face and the reference face
        diff = cv2.absdiff(current_face, reference_face)

        # Compute the mean value of the absolute difference image
        mean_diff = np.mean(diff)

        # If the mean difference is below a certain threshold, set flag to True
        if mean_diff < 20:
            flag = True

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show the frame
    cv2.imshow('frame', frame)

    # If the 'q' key is pressed, break out of the loop
    if cv2.waitKey(1)==True and (0xFF == ord('q')):
        break

    # If the flag is set to True, print a success message and break out of the loop
    if flag:
        print('Face authentication successful!')
        break

# If the flag is not set to True, print an error message
if not flag:
    print('Face authentication unsuccessful!')

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()