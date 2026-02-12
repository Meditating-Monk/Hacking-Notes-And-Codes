#!/usr/bin/env python3

#modules and package imports
import sys

#Authentication function-will verify if master password is correct
def authentication():
    print('for authentication')

#main menu for all options provided to manage passwords    
def menu():
    print('--======PASSMAN======--')
    print('Add Password         a')
    print('View Password        v')
    print('Update Password      u')
    print('Delete Password      d')
    print('List All             l')
    print('Exit                 e')

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
    print('to exit menu')
    sys.exit(0)

#main function code
def main():
    while True:
        
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

        elif selected_option=='e':
            exit()

        else:
            print('Invalid option.')

if __name__=='__main__':
    main()


