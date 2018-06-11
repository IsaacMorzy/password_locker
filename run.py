#!/usr/bin/env python3.6
from credential import Credential
from userData import User
import pyperclip
import sys
import os
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

terminal_width = os.get_terminal_size().columns
def create_new_account(username, password):
    new_account = User(username, password)
    return new_account

def check_username_exists(usern):
    return User.find_user(usern)

def save_account(account):
    account.save_user()

def delete_account(account):
    account.user_delete_account()

def login_user(usern, passw):
    return User.confirm_user(usern,passw)

def user_change_password(usern,newpass):
    return User.change_userpass(usern,newpass)

def create_new_prof(profile_name,profile_username=None,profile_email=None,profile_password=None):
    new_profile = Credential(profile_name,profile_name,profile_username=None,profile_email=None,profile_password=None)
    return new_profile

def save_prof(new_profile):
    new_profile.save_profile()

def delete_prof(profile):
    profile.delete_profile()

def generate_pass(length):
    gen_password = Credential.generate_random_password(length)
    return gen_password

def check_prof_exist(prof_name,prof_username=None,prof_email=None):
    return Credential.check_profile_exist(prof_name,prof_username=None,prof_email=None)


def search_prof(search):
    return Credential.search_profile(search)

def copy_password(search_item):
    return Credential.copy_credentials(search_item)

def display_prof():
    return Credential.display_profiles()

def handle_short_codes(short_code):
    short_code = short_code.lower().replace(" ","")
    if short_code == "np":
        cprint("Wanna create a new profile".center(terminal_width),"blue")
        print("Please enter profile name...eg github")
        profile_name_entered = input()
        if not profile_name_entered:
            cprint("Profile name cannot be blank","red")
        else:
            print("Enter username of the profile account(optional)")
            profile_username_entered =  input()
            print("Enter email of the profile account(optional)")
            profile_email_entered = input()
            print("Enter password of the account(optional)")
            profile_pass_entered = input()
            prof_new = Credential(profile_name_entered,profile_username_entered,profile_email_entered,profile_pass_entered)
            prof_exist = check_prof_exist(profile_name_entered,profile_username_entered,profile_email_entered)
            if prof_exist:
                print("\n")
                cprint("Profile already exist".center(terminal_width),"red")
                print("\n")

            else:
                if not save_prof(prof_new):
                    print("\n")
                    cprint("New profile created".center(terminal_width),"green")
                    print("\n")
                else:
                    print("\n")
                    cprint("Profile has not been created.Try Again".center(terminal_width),"red")
                    print("\n")

    elif short_code == "dp":
        show_prof = display_prof()
        if not show_prof:
            print("\n")
            cprint("NO PROFILE SAVED IN YOUR ACCOUNT".center(terminal_width),"red")
            print("\n")
        else:
            cprint("Here is a list of all your profiles".center(terminal_width),"blue")
            print("\n")
            print(("-*-"*25).center(terminal_width))

            for profile in display_prof():
                print(f"PROFILE NAME:{profile.profile_name}".center(terminal_width))
                print(f"PROFILE USERNAME:{profile.profile_username}".center(terminal_width))
                print(f"PROFILE EMAIL:{profile.profile_email}".center(terminal_width))
                print(f"PROFILE PASSWORD:{profile.profile_password}".center(terminal_width))
                print(("-*-"*25).center(terminal_width))
                print("\n")

    elif short_code == "gp":
        print("Enter the profile name you want to generate password for")
        profile_gen_passwd = input()
        profile_to_change = search_prof(profile_gen_passwd)
        if profile_to_change:
            print("Enter the length of the password you want:")
            passwd_length = input()
            try:
                    pwd_length = int(passwd_length)
                    if passwd_length.isdigit():
                        new_passwd = generate_pass(pwd_length)
                        profile_to_change.profile_password = new_passwd
                        print("\n")
                        cprint("New Password Generated and Saved successfully".center(terminal_width), "green")
                        print("\n")
                    else:
                        cprint("\t Negative numbers are not allowed", "red")
                        print("\n")
            except ValueError:
                cprint("\tYou must enter a number...eg 6", "red")
                print("\n")
        else:
            print("\n")
            cprint("There is no profile with that name".center(terminal_width), "red")
            print("\n")

    elif short_code=="search":
        print("Enter your search")
        search_string = input()
        if search_string:
            search_res =  search_prof(search_string)
            if search_res:
                print("\n")
                cprint("SEARCH RESULTS".center(terminal_width),"green")
                print("\n")
                print(("-*-"*25).center(terminal_width))
                print(f"PROFILE NAME:{search_res.profile_name}".center(terminal_width))
                print(f"PROFILE USERNAME:{search_res.profile_username}".center(terminal_width))
                print(f"PROFILE EMAIL:{search_res.profile_email}".center(terminal_width))
                print(f"PROFILE PASSWORD:{search_res.profile_password}".center(terminal_width))
                print(("-*-"*25).center(terminal_width))
                print("\n")
            else:
                print("\n")
                cprint("No items found using that criteria".center(terminal_width),"magenta")
                print("\n")
        else:
            cprint("You must enter a search item","red")

    elif short_code == "copy":
        print("Enter the profile you want to copy(password)")
        search_passw = input()
        found_copy_prof = search_prof(search_passw)
        if not search_passw:
            cprint("You must enter the profile you want to copy password","red")
        else:
            if not found_copy_prof:
                cprint("\tProfile not found!","red",attrs=["bold"])
            else:
                copy_success = copy_password(search_passw)
                paste_passwd = pyperclip.paste()
                if paste_passwd:
                    cprint("\t Copied!!","green")
                    print("\n")
                else:
                    cprint("\t Not copied!!!","red")
                    print("\n")

    elif short_code == "del":
        cprint("PROCEED WITH CAUTION!".center(terminal_width),"red",attrs=["bold","blink"])
        print("Enter the name of the profile you want to delete:")
        del_profile = input()
        found_prof = search_prof(del_profile)
        if found_prof:
            cprint("DO YOU WANT TO CONTINUE TO DELETE? Y/N",attrs=["bold"])
            continue_prompt = input().upper()
            if continue_prompt == "Y":
                delete_prof(found_prof)
                print("\n")
                cprint("Profile Deleted!".center(terminal_width),"green")
                print("\n")
            elif continue_prompt=="N":
                return
            else:
                cprint("\t You entered an unrecognised command","red")
        else:
            print("\n")
            cprint("The profile does not exist".center(terminal_width),"red")
            print("\n")

    elif short_code=="acp":
        cprint("WE NEED TO CONFIRM ITS YOU!".center(terminal_width),"red",attrs=['bold','blink'])
        print("Enter your username")
        passwd_change_username = input()
        print("Enter your account password")
        passwd_change_password = input()
        if not (passwd_change_password or passwd_change_username):
            cprint("You submitted empty field(s)")
            print("\n")
        else:
            data_match = login_user(passwd_change_username,passwd_change_password)
            if data_match:
                print("Enter your new password")
                new_entered_passwd = input()
                print("Confirm password")
                confirm_entered_passwd = input()
                if new_entered_passwd == confirm_entered_passwd:
                    user_change_password(passwd_change_username,new_entered_passwd)
                    print("\n")
                    cprint("Password changed","green")
                    print("\n")
                else:
                    print("\n")
                    cprint("Password confirmation does not match","red")
                    print("\n")
            else:
                print("\n")
                cprint("Error, please check your login details and try again","red")
                print("\n")

    elif short_code=="delete":
        cprint("WE NEED TO CONFIRM ITS YOU!".center(terminal_width),"red",attrs=["bold","blink"])
        print("Enter your username")
        passwd_change_username = input()
        print("Enter your account password")
        passwd_change_password = input()
        if not (passwd_change_password or passwd_change_username):
            cprint("You submitted empty field(s)")
            print("\n")
        else:
            data_match = login_user(passwd_change_username,passwd_change_password)
            user_acc = user_change_password(passwd_change_username,passwd_change_password)
            if data_match:
                delete_account(user_acc)
                print("\n")
                cprint("User deleted","green")
                print("\n")
                return
            else:
                print("\n")
                cprint("Error, please check your acc details and try again","red")
                print("\n")


    elif short_code=="logout":
        return

    elif short_code == "ex":
        cprint("\t BYE. . ...","cyan")
        sys.exit()
    else:
        print("\n")
        cprint("You entered an unrecognised command".center(terminal_width),"red")
        print("\n")

def main():
    try:
        cprint(figlet_format('cipher', font='starwars'),'blue', attrs=['bold'])
        cprint("\033[1m" +  "Hello, Welcome to cipher".center(terminal_width),"white", attrs=['bold','blink'])
        while True:
            print("Already have an account? Y/N")
            account_prompt = input().upper().strip()
            if account_prompt == "Y":
                print("Enter your username:")
                existing_username = input()
                if not existing_username:
                    cprint("You have not entered a username !","red")
                    print("Enter your username:")
                    existing_username = input()
                print("Enter your password:")
                existing_password = input()
                if not existing_password:
                    cprint("You have not entered a password!","red")
                    print("Enter your password:")
                    existing_password = input()
                login_success = login_user(existing_username, existing_password)
                if not login_success:
                    print("\n")
                    cprint("Incorrect username / password combination","red")
                    print("\n")
                else:
                    while True:
                        print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : np - Add a new profile, dp-Display all profiles, gp - generate new password for a profile, search - find a profile, copy - copy password to clipboard, del - delete a profile, logout- logout of session, ex - exit the application")
                        print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
                        short_code = input()
                        handle_short_codes(short_code)
                        if short_code=="logout" or short_code=="delete":
                            break

            elif account_prompt == "N":
                print("Enter your details to create a new account".center(terminal_width))
                print("Please enter your preffered username")
                new_user_username = input()
                if not new_user_username:
                    cprint("You have not entered any username!","red")
                    new_user_username = input()
                print("Please enter your password")
                new_user_password = input()
                if not new_user_password:
                    cprint("You have not entered any password!","red")
                    new_user_password = input()
                user_already_exist = check_username_exists(new_user_username)
                if not user_already_exist:
                    user_new = User(new_user_username,new_user_password)
                    if not save_account(user_new):
                        print("\n")
                        cprint("\033[1m Account created successfully \033[0m".center(terminal_width),"green")
                        print("\n")
                        while True:
                            print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : np - Add a new profile, dp-Display all profiles, gp - generate new password for a profile, search - find a profile, copy - copy password to clipboard, del - delete a profile, logout- logout of session,  ex - exit the application")
                            print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
                            short_code = input()
                            handle_short_codes(short_code)
                            if short_code=="logout" or short_code=="delete":
                                break
                else:
                    print("\n")
                    cprint("The username is already in use","magenta")
                    cprint("Please try another username","magenta")
                    print("\n")

            else:
                print("\n")
                cprint("You have entered unrecognised command...Please enter Y/N!","red")
                print("\n")
    except KeyboardInterrupt:
           print("\n")
           cprint("An interrupt detected...Exiting..", "yellow", attrs=["bold"])
           sys.exit()

if __name__=="__main__":
    main()