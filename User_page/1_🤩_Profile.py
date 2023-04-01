import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth
import database as db

st.set_page_config(
    page_title="ChunkyMonkeys",
    page_icon="🐵",
)

st.title("Profile")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

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
        s,t,q = st.columns(3)
        with s:
            st_lottie(ani2,height=100,key="monkey1")
        with t:
            st.title(":violet[ChnkyMnks]")
        with q:
            st_lottie(ani2,height=100,key="monkey2") 

    st.write("---")
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
