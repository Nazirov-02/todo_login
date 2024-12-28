from random import choice
from auth import register,login,logout
from db import set_false_resent_all,show_resent_user,log_out,check_role,is_authenticated,show_all_users,update_admin
from session import Session

def admin_window():
    choice = input(f"""
    1.Add new admin
    2.Delete admin
    3.Add todo 
    4.update todo
    5.Delete todo
    6.Show all todos
    7.Show all users date
    8.Delete user
    9.Log out
    10.Back
    >>>: """)
    if choice == '1':
        user_name = input('Enter user name: ')
        role = 'admin'
        if not is_authenticated(user_name):
          if update_admin(user_name,role):
             print('New admin successfully added')
          admin_window()
        print('Something wrong with user name please check and try again')
        admin_window()

    elif choice == '2':
        user_name = input('Enter user name: ')
        role = 'user'
        if not is_authenticated(user_name):
          if update_admin(user_name,role):
             print('Admin delete successfully')
          admin_window()
        print('Something wrong with user name please check and try again')
        admin_window()
    elif choice == '3':
         pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        counter = 1
        data = show_all_users()
        for user in data:
            print(f'{counter})user name:{user[1]}, role:{user[4]}, created at:{user[-1]}')
            counter += 1
        admin_window()
    elif choice == '8':
        user_name = input('Enter user name: ')
        if not is_authenticated(user_name):
            log_out(user_name)
            print('User successfully delete')
        else:
            print('Something wrong with user name please check and try again !')
        admin_window()
    elif choice == '9':
        user_name = show_resent_user()
        if log_out(user_name):
            print('Successfully log out !')
            main()
    elif choice == '10':
        set_false_resent_all()
        main()



def user_window():
    choice = input(f"""
    1.Add todo
    2.Update todo
    3.Delete todo
    4.show all todos
    5.Show my all todos
    6.Back
    >>>: """)
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        set_false_resent_all()
        main()


def main():
    choice = input(f"""
    1.Log in 
    2.Register
    3.Exit
    >>>: """)

    if choice == '1':
        if login():
          user = show_resent_user()[0]
          result = check_role(user)
          print(result)
          if result == 'admin':
            admin_window()
          elif result == 'user':
              user_window()
          else:
              print('Some thing is wrong with users role !')
              main()
        print('Wrong input please check and try again !')
        main()
    elif choice == '2':
        if register():
            print('User successfully added')
            print('please Log in !')
        else:
            print('This user already exists please try another one')
        main()
    elif choice == '3':
        print('Thank you for using our services')
        return
    else:
        print("Wrong choice please try again")
        main()

if __name__=="__main__":
    main()