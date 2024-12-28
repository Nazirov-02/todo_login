from typing import Optional
import bcrypt



def hash_password(password):
    default_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(default_password,salt)
    return hashed_password


def match_password(default_password,hashed_password):
    result =  bcrypt.checkpw(default_password.encode('utf-8'),hashed_password.encode('utf-8'))
    return result



class Response:
    def __init__(self,
                 status_code: int = 200,
                 message: Optional[str] = None):
        self.status_code = status_code
        self.message = message


class BadRequest:
    def __init__(self, status_code: int = 404, message: Optional[str] = None):
        self.status_code = status_code
        self.message = message
    def return_(self):
        return self.status_code,self.message
