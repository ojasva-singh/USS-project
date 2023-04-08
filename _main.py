import pyrebase
import streamlit
import streamlit as st
from datetime import datetime
from collections.abc import Mapping
from streamlit_lottie import st_lottie
import requests


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

email = streamlit.sidebar.text_input('Enter your email address')
password = streamlit.sidebar.text_input('Enter your password',type='password')

if choice == 'Sign Up':
    un = streamlit.sidebar.text_input('Please enter a username.',key='1')
    #email = streamlit.sidebar.text_input('Enter your email address',key='2')
    #p1 = streamlit.sidebar.text_input('Enter your password',key='3')
    #p2 = streamlit.sidebar.text_input('Enter your password again',key='4')
    un_sub = streamlit.sidebar.button('Create my account')
    if un_sub == True:
      user = auth.create_user_with_email_and_password(email,password)
      streamlit.success('Account created successfully')
      streamlit.snow()
      user = auth.sign_in_with_email_and_password(email,password)
      db.child(user['localId']).child("Username").set(un)
      #db.child(user)
      db.child(user['localId']).child("ID").set(user['localId'])
      streamlit.title('Welcome ' + un)
      streamlit.info('Please login again through the sidebar')
  
if choice == 'Login':
  #un = streamlit.sidebar.text_input('Please enter your username.')
  login = st.sidebar.checkbox('Login')
  if login:
     user = auth.sign_in_with_email_and_password(email,password)
     st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
     bio = st.radio('Go to',['Community Page','Profile','Contact Me'])

     if bio == 'Community Page':
         st.write("Anckonjcdnkjsndjclnsljdnclsdnvncjldsnjcns")
         
     if bio == 'Profile':
        un_sub = True
        if un_sub:
            authentication_status = True
            if authentication_status == True:
            #st.set_page_config(page_title="Ojasva Singh 🤩🫦", page_icon = "👁️", layout="wide")
                def load_ani(url):
                    req = requests.get(url)
                    if(req.status_code!=200):
                        return None
                    return req.json()

                ani1 = load_ani("https://assets4.lottiefiles.com/packages/lf20_iv4dsx3q.json")
                ani2 = load_ani("https://assets8.lottiefiles.com/packages/lf20_Y8UeVt.json")

                with st.container():
                    st.subheader("Hi, I am Ojasva :wave:")
                    st.title("A Software Developer from India :earth_asia:")
                    st.write("Anything in general makes me curious, I am a table tennis player and i also love to read about neuroscience in my past time. Take a look at my miserable life here,")
                    st.write("[Instagram >](www.instagram.com/ojasvasingh_)")

                with st.container():
                    st.write("---")
                    left_col , right_col = st.columns(2)
                    with left_col:
                        st.header("About me  💁🏽‍♂️")
                        st.write('##')
                        st.write(
                            "I am a student at IIIT Delhi, pursuing Computer Science with Applied Mathematics:mortar_board:.Also I am soon going to be an SDE at Reliance Jio. My favourite language is Java, funny how I am codng in python at this moment.")
                        st.write("Technically this is just a dummy website for our USS project :stuck_out_tongue: so that we could test our authentication system, but I'm getting the vibe that this could be used as a blog page haha :laughing:")
                        st.write("Bubyeeeeee🥰")
                        st.write("Take a look at some of my work/projects")
                        st.write("[Learn More >](https://github.com/lucious20318)")
                    with right_col:
                        st_lottie(ani1,height=320,key="coding")
         
     if bio == 'Contact Me':
         st.title("Get in touch with me")
         def local_css(filename):
             with open(filename) as f:
                st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
                local_css("/Users/ojasvasingh/Desktop/Fin/styles.css")
       
         with st.container():
            st.write("---")
            st.header("You can contact me from here .. 🤝🏽")
            st.write("##")

            contact_form = """
                            <form action="https://formsubmit.co/ojasva963@gmail.com" method="POST">
                                <input type="hidden" name="_captcha" value="false">
                                <input type="text" name="Name" placeholder="Enter your name" required>
                                <input type="email" name="Email" placeholder="Enter your email" required>
                                <textarea name="Message" placeholder="Enter your query" required></textarea>
                                <button type="submit">Send</button>
                            </form>
                        """
            
            left_col , right_col = st.columns(2)
            with left_col:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_col:
                st.empty()