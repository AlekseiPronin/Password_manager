master_pwd = input('Input the master password: ')

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            print(line.rstrip())

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