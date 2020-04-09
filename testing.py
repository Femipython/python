import random
import string


def get_userinfo(first_name, last_name, email):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    return first_name, last_name, email


def gen_password(first_name, last_name):
    letters = string.ascii_lowercase
    length = 5
    random_string = ''.join(random.choice(letters) for i in range(length))
    password = (first_name[0:2] + last_name[1][-2:] + random_string)
    return password


container = []
numberOfUser = 1
status = True
while status:
    get_userinfo(first_name, last_name, email)
    password = gen_password()
    print("The suggested password is: " + str(password))

    want_password = input("Do you want the suggested password saved as your password (type Yes or No): ")

    password_loop = True
    while password_loop:
        if want_password == "Yes":
            print("Your password has been set as " + password)
            password_loop = False

        else:
            new_password = input("Enter desired password(not less than 7 characters): ")

            if len(new_password) >= 7:
                print("Your password has been set as " + new_password)

                password_loop = False

            else:
                print("Your password has less than 7 characters, re-enter.")
                new_password = password
    user = {'first name':first_name, 'last name':last_name, 'e-mail': email, 'password': password}
    data = f"user{numberOfUser} details: {user}"
    new_user = input("Are you a new user(Enter Yes or No): ")

    if new_user == "No":
        status = False
        print(data)
    else:
        status = True
        numberOfUser = numberOfUser + 1








