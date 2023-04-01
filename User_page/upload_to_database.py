import streamlit_authenticator as stauth
import database as db

Names = ["Nakul Periwal", "Ojasva Singh", "Ghosh"]
usernames = ["nakul_periwal","ojasvasingh_" , "milkman"]
pwds = ["nkool","ojool","bunda"]

hashed_pwds = stauth.Hasher(pwds).generate()

for(username, name, hashed_pwd) in zip(usernames, Names, hashed_pwds):
    db.insert_user(username,name,hashed_pwd)