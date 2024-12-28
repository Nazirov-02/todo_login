from typing import Optional
from models import User



class Session:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, session: Optional[User]= None ):
        self.session = session

    def add_session(self, user: User):
        self.session = user

    def check_session(self):
        return self.session

#
# session = Session()
# user = User('alo','1234')
# session.add_session(user)
# curr = session.check_session()
# print(curr.username)
