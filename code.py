pwd = input('Input the master password: ')

while True:
    mode = input('Add the new password or view the existing one (view, add)? Press q for quit').lower()
    if mode == 'q':
        break

    
    if mode == 'view':
        pass
    elif mode == 'add':
        pass
    else:
        print('Invalid mode')