
from db import is_authenticated,migrate,set_true_resent_user
from models import User
from utils import match_password

def login():
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    if  is_authenticated(user_name,password):
       set_true_resent_user(user_name)
       return True
    return False

def logout():
    pass


def register():
    user_name = input("Enter your user name: ")
    if not is_authenticated(user_name):
        return False
    password = input("Enter your password: ")
    user = User(username=user_name,password=password)
    if migrate(user.return_data()):
        return True


