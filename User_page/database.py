from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv(".env")
Deta_key = os.getenv("Deta_key")
deta = Deta(Deta_key)

db = deta.Base("Dummy_base")

def insert_user(username , name , pwd):
    return db.put({"key": username, "name": name, "password": pwd})

def get_user(username):
    return db.get(username)

def update_user(username, updates):
    return db.update(updates, username)

def fetch_all_users():
    result = db.fetch()
    return result.items

#update_user("ojasvasingh_" , {"name": "Vishu Singh"})
