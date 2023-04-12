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
      try:
        user = auth.create_user_with_email_and_password(email,password)
      except:
          st.error("Invalid Credentials, Please login again.")
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
     try:
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>',unsafe_allow_html=True)
        bio = st.radio('Go to',['Community Page','New Post','Profile','Contact Me'])

        if bio == 'Community Page':
            all_users = db.get()
            res = []
            #store users handle name
            for item in all_users.each():
                un_val = item.val()["Username"]
                res.append(un_val)
                
            #Total users
            n = len(res)
            st.write('Total users here: '+str(n))

            #Choice for selecting a different user
            choice = st.selectbox('Peope',res)
            c1,c2,c3 = st.columns(3)
            with c1:
                push1 = st.button('Show Post')
            with c2:
                push2 = st.button("Show Profile")

            if push1:
                st.write("\n")
                st.write("\n")
                for item in all_users.each():
                    i_val = item.val()["Username"]
                    if i_val == choice:
                        uid = item.val()["ID"]
                        usn = db.child(uid).child("Username").get().val()
                        st.markdown(usn,unsafe_allow_html=True)

                        nimg = db.child(uid).child("Image").get().val()
                        if nimg is not None:
                            val = db.child(uid).child("Image").get()
                            for item in val.each():
                                img_choice = item.val()
                                c1,c2,c3 = st.columns(3)
                                with c2:
                                    st.image(img_choice)
                        else:
                            st.info("Profile Picture not updated")
                        
                        all_post = db.child(uid).child("Posts").get()
                        if all_post.val() is not None:
                            for item in reversed(all_post.each()):
                                st.write(item.val())
            
            if push2:    
                st.write("\n")
                st.write("\n")
                for item in all_users.each():
                    i_val = item.val()["Username"]
                    if i_val == choice:
                        uid = item.val()["ID"]
                        usn = db.child(uid).child("Username").get().val()
                        st.markdown(usn,unsafe_allow_html=True)

                        nimg = db.child(uid).child("Image").get().val()
                        if nimg is not None:
                            val = db.child(uid).child("Image").get()
                            for item in val.each():
                                img_choice = item.val()
                                c1,c2,c3 = st.columns(3)
                                with c2:
                                    st.image(img_choice)
                        else:
                            st.info("Profile Picture not updated")

                        def load_ani(url):
                            req = requests.get(url)
                            if(req.status_code!=200):
                                return None
                            return req.json()
            
                        with st.container():
                                #name = db.child(user['localId']).child("Information").child("Name").get()
                                name = db.child(uid).child("Information").child("Name").get()
                                if name.val() is not None:
                                    for item in name.each():
                                        fin = item.val()
                                    st.subheader(fin)

                                prof = db.child(uid).child("Information").child("Bio").get()
                                if prof.val() is not None:
                                    for item in prof.each():
                                        fin = item.val()
                                    st.title(fin)

                                br_desc = db.child(uid).child("Information").child("descr").get()
                                if br_desc is not None:
                                    if br_desc.each() is not None:
                                        for item in br_desc.each():
                                            fin = item.val()
                                        st.write(fin)
                                sm = db.child(uid).child("Information").child("SocialMedia").get()
                                if sm is not None and sm.each() is not None:
                                    for item in sm.each():
                                        fin = item.val()
                                    st.write(fin)

                        about = db.child(uid).child("Information").child("About").get()
                        if about is not None and about.each() is not None:
                            with st.container():
                                    st.write("---")
                                    left_col , right_col = st.columns(2)
                                    with left_col:
                                        st.header("About me  💁🏽‍♂️")
                                        st.write('##')
                                        for item in about.each():
                                            fin = item.val()
                                        st.write(fin)
                                    with right_col:
                                        an1 = db.child(uid).child("Information").child("Lottie").get()
                                        if an1 is not None:
                                            for item in an1.each():
                                                fin = item.val()
                                            ani1 = load_ani(fin)
                                            st_lottie(ani1,height=320,key="coding")
                            


        if bio == 'New Post':
            st.write("\n")
            st.write("\n")
            c1,c2 = st.columns(2)
            with c1:
                nimg = db.child(user['localId']).child("Image").get().val()
                if nimg is not None:
                    val = db.child(user['localId']).child("Image").get()
                    for item in val.each():
                        item_choice = item.val()
                    st.image(item_choice,use_column_width=True)
                else:
                    st.info("No picture uploaded yet, you can do so by going to your profile page")
                
                post = st.text_input("Share what's on your head!!",max_chars=150)
                add_post = st.button('Share post')
                if add_post:
                    cur = datetime.now()
                    dt_string = cur.strftime("%d/%m/%Y %H:%M:%S")
                    post = {'Caption:' : post,
                            'Time': dt_string}
                    result = db.child(user['localId']).child("Posts").push(post)

            with c2:
                #c1.header('')
                all_post = db.child(user['localId']).child("Posts").get()
                if all_post.val() is not None:
                    for item in reversed(all_post.each()):
                        st.write(item.val())

            
        if bio == 'Profile':
            st.write("\n")
            st.write(("\n"))
            #Check for image
            pimg = db.child(user['localId']).child("Image").get().val()
            #If image is found
            if pimg is not None:
                img = db.child(user['localId']).child("Image").get()
                for item in img.each():
                    i_choice = item.val()
                
                c1,c2,c3 = st.columns(3)
                
                with c2:
                    st.image(i_choice)
                
                def load_ani(url):
                        req = requests.get(url)
                        if(req.status_code!=200):
                            return None
                        return req.json()
                
                with st.container():
                        #name = db.child(user['localId']).child("Information").child("Name").get()
                        name = db.child(user['localId']).child("Information").child("Name").get()
                        if name.val() is not None:
                            for item in name.each():
                                fin = item.val()
                            st.subheader(fin)

                        prof = db.child(user['localId']).child("Information").child("Bio").get()
                        if prof.val() is not None:
                            for item in prof.each():
                                fin = item.val()
                            st.title(fin)

                        br_desc = db.child(user['localId']).child("Information").child("descr").get()
                        if br_desc is not None:
                            for item in br_desc.each():
                                fin = item.val()
                            st.write(fin)
                        sm = db.child(user['localId']).child("Information").child("SocialMedia").get()
                        if sm is not None:
                            for item in sm.each():
                                fin = item.val()
                            st.write(fin)

                about = db.child(user['localId']).child("Information").child("About").get()
                if about is not None:
                    with st.container():
                            st.write("---")
                            left_col , right_col = st.columns(2)
                            with left_col:
                                st.header("About me  💁🏽‍♂️")
                                st.write('##')
                                for item in about.each():
                                    fin = item.val()
                                st.write(fin)
                            with right_col:
                                an1 = db.child(user['localId']).child("Information").child("Lottie").get()
                                if an1 is not None:
                                    for item in an1.each():
                                        fin = item.val()
                                    ani1 = load_ani(fin)
                                    st_lottie(ani1,height=320,key="coding")

                exp = st.expander('Change bio and image')
                with exp:
                    newimgpath = st.text_input('Enter the path of your image')
                    upload_new = st.button('Upload')
                    if upload_new:
                        uid = user['localId']
                        fireb_upload = storage.child(uid).put(newimgpath,user['idToken'])
                        a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                        db.child(user['localId']).child("Image").push(a_imgdata_url)
                        #st.success('Successfully uploaded!')
                    
                    name = st.text_input('Enter your name')
                    upload_new = st.button('Upload',key=1)
                    if upload_new:
                        uid = user['localId']
                        result = db.child(uid).child("Information").child("Name").push(name)
                        #st.success('Successfully uploaded!')
                    
                    prof = st.text_input('Enter your bio')
                    upload_new = st.button('Upload',key=2)
                    if upload_new:
                        uid = user['localId']
                        result = db.child(uid).child("Information").child("Bio").push(prof)
                        #st.success('Successfully uploaded!')
                    
                    an1 = st.text_input('You can choose an animation URL to fancy your profile from the below website')
                    st.write("https://lottiefiles.com")
                    upload_new = st.button('Upload',key=3)
                    if upload_new:
                        uid = user['localId']
                        result = db.child(uid).child("Information").child("Lottie").push(an1)
                        #st.success('Successfully uploaded!')
                    
                    br_desc = st.text_input('Enter a brief description about yourself')
                    upload_new = st.button('Upload',key=4)
                    if upload_new:
                        uid = user['localId']
                        result = db.child(uid).child('Information').child("descr").push(br_desc)
                    
                    sm_handle =  st.text_input('Enter your social media handle')
                    upload_new = st.button('Upload',key=5)
                    if upload_new:
                        uid = user['localId']
                        result = db.child(uid).child('Information').child("SocialMedia").push(sm_handle)
                    
                    pr_desc = st.text_input('Tell people more about yourself')
                    upload_new = st.button('Upload',key=6)
                    if upload_new:
                        uid = user['localId']
                        result = db.child(uid).child('Information').child("About").push(pr_desc)
                    

            #If no image is found
            else:
                #st.info("No profile picture yet")
                newimgpath = st.text_input('Enter the path of your image')
                upload_new = st.button('Upload')
                if upload_new:
                    uid = user['localId']
                    #Stored initiated bucket in firebase
                    fireb_upload = storage.child(uid).put(newimgpath,user['idToken'])
                    #URL for easy access
                    a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                    #Put in realtime database
                    db.child(user['localId']).child("Image").push(a_imgdata_url)

                name = st.text_input('Enter your name')
                upload_new = st.button('Upload',key=1)
                if upload_new:
                    uid = user['localId']
                    result = db.child(uid).child("Information").child("Name").push(name)
                    #st.success('Successfully uploaded!')
                
                prof = st.text_input('Enter your bio')
                upload_new = st.button('Upload',key=2)
                if upload_new:
                    uid = user['localId']
                    result = db.child(uid).child("Information").child("Bio").push(prof)
                    #st.success('Successfully uploaded!')
                
                an1 = st.text_input('You can choose an animation URL to fancy your profile from the below website')
                st.write("https://lottiefiles.com")
                upload_new = st.button('Upload',key=3)
                if upload_new:
                    uid = user['localId']
                    result = db.child(uid).child("Information").child("Lottie").push(an1)
                    #st.success('Successfully uploaded!')
                
                br_desc = st.text_input('Enter a brief description about yourself')
                upload_new = st.button('Upload',key=4)
                if upload_new:
                    uid = user['localId']
                    result = db.child(uid).child('Information').child("descr").push(br_desc)
                
                sm_handle =  st.text_input('Enter your social media handle')
                upload_new = st.button('Upload',key=5)
                if upload_new:
                    uid = user['localId']
                    result = db.child(uid).child('Information').child("SocialMedia").push(sm_handle)
                
                pr_desc = st.text_input('Tell people more about yourself')
                upload_new = st.button('Upload',key=6)
                if upload_new:
                    uid = user['localId']
                    result = db.child(uid).child('Information').child("About").push(pr_desc)


            un_sub = False
            if un_sub:
                authentication_status = True
                if authentication_status == True:
                    def load_ani(url):
                        req = requests.get(url)
                        if(req.status_code!=200):
                            return None
                        return req.json()

                    ani1 = load_ani("https://assets4.lottiefiles.com/packages/lf20_iv4dsx3q.json")
                    #ani2 = load_ani("https://assets8.lottiefiles.com/packages/lf20_Y8UeVt.json")

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

     except:
         st.error("Invalid Credentials please login again")
    