import streamlit as st

st.title("Get in touch with me")

def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    
local_css("/Users/ojasvasingh/Desktop/DummyWb/streamlit-multipage-app-example-master/pages/styles.css")

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