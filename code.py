from cryptography.fernet import Fernet



'''the wrong key still allows you to look through the password file'''

# # Write key function
# # calling function only once to create "key" file, comment out after simgle use
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", 'wb') as key_file:
#         key_file.write(key)

# write_key()

# Load Key function
def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


# Creating master password
master_pwd = input('Input the master password: ')

# Encode converts into bytes
key = load_key() + master_pwd.encode()

# initializing encription module
fer = Fernet(key)

# View the list of created passwords. Decrypting previously encrypted pwd
def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print('User: ', user, ', Password: ',
                fer.decrypt(passw.encode()).decode())

# Adding new passwords function. decoding the encrypted password that was encoded.
# Encoding converts pwd into bytes
def add():
    name = input('Account Name: ')
    pwd = input('Account Password: ')

    with open('passwords.txt', 'a') as file:
        file.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')

# Create infinite loop in case we need to write multiple pwds. 
# Quits after pressing 'q'
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