import pyrebase
import streamlit
from datetime import datetime
from collections.abc import Mapping

#Firebase config key
firebaseConfig = {
  'apiKey': "AIzaSyC9T-1ZY4ohukBLB2KBZeN2b-qR6PUP-0Q",
  'authDomain': "ussproject-656d4.firebaseapp.com",
  'projectId': "ussproject-656d4",
  'databaseURL': "https://ussproject-656d4-default-rtdb.europe-west1.firebasedatabase.app",
  'storageBucket': "ussproject-656d4.appspot.com",
  'messagingSenderId': "521612277321",
  'appId': "1:521612277321:web:c300d84ed956f6a32d3198",
  'measurementId': "G-EZCSBNH2LY"
} 

#Firebase Authentication
firebase = pyrebase .initialize_app(firebaseConfig)
auth = firebase.auth()

#Database
db = firebase.database()
storage = firebase.storage()
streamlit.sidebar.title("Welcome to ChunkyMonkeys 🐵")

#Authentication

choice = streamlit.sidebar.selectbox('Login/SignUp',['Login','Sign Up'])

#email = streamlit.sidebar.text_input('Enter your email address')
#password = streamlit.sidebar.text_input('Enter your password')
p2 = ''
if choice == 'Sign Up':
    un = streamlit.sidebar.text_input('Please enter a username.')
    email = streamlit.sidebar.text_input('Enter your email address')
    p1 = streamlit.sidebar.text_input('Enter your password')
    #p1 = 'aaaaaa'
    #if(len(p1) < 6):
       #streamlit.warning("Length of passowrd should be equal or greater than 6")
    p2 = streamlit.sidebar.text_input('Enter your password again')
    #p2 = 'aaaaaa'
    #if(p1 != p2):
        #streamlit.warning("Passwords don't match, renter your password.")
if p2:
  un_sub = streamlit.sidebar.button('Create my account')
  if un_sub == True:
    user = auth.create_user_with_email_and_password(email,p1)
    streamlit.success('Account created successfully')
    streamlit.balloons()
    user = auth.sign_in_with_email_and_password(email,p1)
    db.child(user['localId']).child("Username").set(un)
    db.child(user['localId']).child("ID").set(user['localId'])
    streamlit.title('Welcome' + un)
    streamlit.info('Please login again through the sidebar')
    
  
if choice == 'Login':
  un = streamlit.sidebar.text_input('Please enter your username.')
  p3 = streamlit.sidebar.text_input('Enter your password')
  streamlit.success('Logged in successfully')