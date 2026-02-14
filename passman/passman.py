#!/usr/bin/env python3

#modules and package imports
import sys
import hashlib
import getpass
import json





#global veriables


auth_bool=False


#Password creation 
def change_master_passwd():
    master_passwd = getpass.getpass('Create your Password: ')
    temp_verification = getpass.getpass('Enter above Password: ')
    if master_passwd == temp_verification:
        temp_data = {
            "master_passwd_hash": hashlib.sha512(master_passwd.encode("utf-8")).hexdigest()
        }
        with open("./config.json",'w') as f:
            json.dump(temp_data,f,indent=4)

        print("Master Password Set")
        global auth_bool
        auth_bool = True
    else:
        print("The passwords didn't match.")





#Authentication function-will verify if master password is correct
def authentication():
    for i in range(1,4):
        input_passwd = getpass.getpass('Input Your Password: ')
        with open("./config.json","r")as f:
            temp_data = json.load(f)
        if temp_data["master_passwd_hash"] == hashlib.sha512(input_passwd.encode("utf-8")).hexdigest():
            global auth_bool
            auth_bool = True
            print('Welcome !')
            break
        else :
            print('Wrong Password.')
            print('You have ',(3-i),' more attempts left')




#main menu for all options provided t:o manage passwords    
def menu():
    print('\n--======PASSMAN======--')
    print('Add Password                                 a')
    print('View Password                                v')
    print('Update Password                              u')
    print('Delete Password                              d')
    print('List All                                     l')
    print('Change Master Password                       c')
    print('Exit                                         e')
    



#codes for all functions    
def add_passw():
    print('for adding')

def view_passw():
    print('for viewing')

def update_passw():
    print('for updating')

def delete_passw():
    print('for deleting')

def list_passw():
    print('for listing')

def exit():
    sys.exit(0)

#main function code
def main():

    with open("./config.json","r") as f:
        if not f.read(1):
            change_master_passwd()
        else:
            authentication()


    while True:       

        if auth_bool == True:
            menu()
        
            selected_option=input('Select option: ')

            if selected_option=='a':
                add_passw()

            elif selected_option=='v':
                view_passw()

            elif selected_option=='u':
                update_passw()

            elif selected_option=='d':
                delete_passw()

            elif selected_option=='l':
                list_passw()

            elif selected_option =='c':
                change_master_passwd()

            elif selected_option=='e':
                exit()

            else:
                print('Invalid option.')
        else:
            exit()

if __name__=='__main__':
    main()


