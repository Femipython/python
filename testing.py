import random
import string


def get_userinfo():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    userinfo = [first_name, last_name, email]
    return userinfo


def gen_password(userinfo):
    letters = string.ascii_lowercase
    length = 5
    random_string = ''.join(random.choice(letters) for i in range(length))
    password = (userinfo[0][:2] + userinfo[1][-2:] + random_string)
    return password


container = []
numberOfUser = 1
status = True
while status:
    userinfo = get_userinfo()
    password = gen_password(userinfo)
    print("The suggested password is: " + str(password))

    want_password = input("Do you want the suggested password saved as your password (type Yes or No): ")

    password_loop = True
    while password_loop:
        if want_password == "Yes":
            print("Your password has been set as " + password)
            userinfo.append(password)
            password_loop = False
        else:
            new_password = input("Enter desired password(not less than 7 characters): ")
            if len(new_password) >= 7:
                print("Your password has been set as " + new_password)
                userinfo.append(new_password)
                password_loop = False
            else:
                print("Your password has less than 7 characters, re-enter.")
                new_password = password
                
    user = {'first name': userinfo[0], 
           'last name': userinfo[1], 
           'e-mail': userinfo[2], 
           'password': userinfo[3]}
    data = f"user{numberOfUser} Information: {user}"
    print(data)
    container.append(data)
    
    new_user = input("Are you a new user(Enter Yes or No): ")
    if new_user == "No":
        status = False
    else:
        status = True
        numberOfUser = numberOfUser + 1
print(container)
        
