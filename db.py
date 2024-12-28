import psycopg2
from utils import Response

db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'KA1275147',
    'database': 'exam',
    'port': 5432
}

conn = psycopg2.connect(**db_info)
cur = conn.cursor()


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper

@commit
def is_authenticated(user_name,password = None):
    if password is None:
       query = """SELECT password FROM USERS
               WHERE username = %s;"""
       data = (user_name,)
       cur.execute(query, data)
       result = cur.fetchone()
       if result is None:
           return True
       return False

    else:
       query = """SELECT password FROM USERS
            WHERE username = %s AND password = %s ;"""
       data = (user_name,password)
    cur.execute(query, data)
    result = cur.fetchone()
    if result is None:
        return False
    if password == result[0]:
     return True


def show_all_users():
    cur.execute('''SELECT * FROM users;''')
    data = cur.fetchall()
    return data


@commit
def create_table_user():
    query = '''CREATE TABLE IF NOT EXISTS users(
            id serial primary key ,
            username varchar(200),
            password text , 
            login_try_count int default 0,
            role varchar(20),
            status boolean default False,
            created_at timestamptz default current_timestamp
    );'''

    cur.execute(query)
    return Response(201, 'User Created')


@commit
def create_table_todo():
    query = '''CREATE TABLE IF NOT EXISTS todos(
        id serial primary key,
        title varchar(200),
        description text,
        todo_type varchar(20) ,
        user_id int references users(id) on delete CASCADE
    );
    '''
    cur.execute(query)
    return Response(201, 'Todo Created')

@commit
def set_true_resent_user(user_name):
    query = """UPDATE users 
               SET status = TRUE
               WHERE username = %s;"""
    data = (user_name,)
    cur.execute(query,data)

@commit
def set_false_resent_all():
    query = """UPDATE users 
               SET status = False
               WHERE status = %s;"""
    data = (True,)
    cur.execute(query,data)

def show_resent_user():
    cur.execute("""SELECT username from users
                   WHERE status = TRUE;""")
    result = cur.fetchone()
    return result


@commit
def migrate(data):

    query = '''insert into users(username, password, login_try_count,role)
    values (%s,%s,%s,%s);'''
    print(data)
    cur.execute(query,data)
    return True

@commit
def log_out(user_name):
  try:
    query = """DELETE FROM users
               WHERE username = %s;"""
    data = (user_name,)
    cur.execute(query,data)
    return True
  except Exception as e:
      print('Some thing is wrong please check and try again !')


def check_role(user_name):
    query = """SELECT role FROM users
               WHERE username = %s;"""
    data = (user_name,)
    cur.execute(query,data)
    result = cur.fetchone()[0]
    return result
@commit
def update_admin(user_name,status):
    query = """UPDATE users
               SET role = %s
               WHERE username = %s;"""
    data = (status,user_name)
    cur.execute(query,data)
    return True

# migrate()
# create_table_user()
# create_table_todo()