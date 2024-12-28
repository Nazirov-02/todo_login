from datetime import datetime
from enum import Enum
from db import migrate
from utils import hash_password

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'


class TodoType(Enum):
    CREATED = 'created'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'



# bu class userni ma'lumotlarni olish va yuborishda ishlatiladi
# bu yerda role defaul holatda UserRole.ADMIN.value = admin ga teng uni UserRole.USER.value = userga tenglasak user windowdan ham foydalansa bo'ladi

class User:
    def __init__(self,
                 username,
                 password,
                 user_id = None,
                 login_try_count = None,
                 role = None ,
                 created_at = None
                 ):
        self.username = username
        self.password = password
        self.login_try_count = login_try_count or 1
        self.role = role or UserRole.ADMIN.value
        self.id = user_id
        self.created_at = created_at or datetime.now()

    def return_data(self):
          data =(self.username,self.password,self.login_try_count,self.role)
          return data
# d = user.return_data()
# print(d)
# #
# class Todo:
#     def __init__(self, todo_id,
#                  title,
#                  description,
#                  todo_type,
#                  user_id
#                  ):
#         self.id = todo_id
#         self.title = title
#         self.description = description
#         self.todo_type = todo_type
#         self.user_id = user_id
