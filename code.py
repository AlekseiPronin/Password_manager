from cryptography.fernet import Fernet

master_pwd = input('Input the master password: ')

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as key_file:
#         key_file.write(key)

# write_key()


def read_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print('User: ', user, ', Password: ', passw)

def add():
    name = input('Account Name: ')
    pwd = input('Account Password: ')

    with open('passwords.txt', 'a') as file:
        file.write(name + ' | ' + pwd + '\n')


while True:
    mode = input('Add the new password or view the existing one (view, add)? Press q for quit  ').lower()
    if mode == 'q':
        break


    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode')