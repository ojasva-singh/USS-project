import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Ojasva Singh 🤩🫦", page_icon = "👁️", layout="wide")

def load_ani(url):
    req = requests.get(url)
    if(req.status_code!=200):
        return None
    return req.json()

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    
local_css("style/styles.css")

ani1 = load_ani("https://assets4.lottiefiles.com/packages/lf20_iv4dsx3q.json")
ani2 = load_ani("https://assets8.lottiefiles.com/packages/lf20_Y8UeVt.json")

with st.container():
    s,t,q,w,e,r,t,y,u,i,l = st.columns(11)
    with w:
        st_lottie(ani2,height=100,key="monkey1")
    with e:
        st.title(":violet[ChunkymonkeyS]")
    with y:
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
        st.header("What I do  💁🏽‍♂️")
        st.write('##')
        st.write(
            "I am a student at IIIT Delhi, pursuing Computer Science with Applied Mathematics:mortar_board:.Also I am soon going to be an SDE at Reliance Jio. My favourite language is Java, funny how I am codng in python at this moment.")
        st.write("Technically this is just a dummy website for our USS project :stuck_out_tongue: so that we could test our authentication system, but I'm getting the vibe that this could be used as a blog page haha :laughing:")
        st.write("Bubyeeeeee🥰")
        st.write("Take a look at some of my work/projects")
        st.write("[Learn More >](https://github.com/lucious20318)")
    with right_col:
        st_lottie(ani1,height=320,key="coding")  


with st.container():
    st.write("---")
    st.header("You can contact me from here .. 🤝🏽")
    st.write("##")

    contact_form = """
                    <form action="https://formsubmit.co/ojasva963@gmail.com" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="Name" placeholder="Your name" required>
                        <input type="email" name="Email" placeholder="Your email" required>
                        <textarea name="Message" placeholder="Your message here" required></textarea>
                        <button type="submit">Send</button>
                    </form>
                """
    
    left_col , right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()
