from firebase import firebase
import random

#Database connection

firebase = firebase.FirebaseApplication("https://password-database-df4db-default-rtdb.firebaseio.com/" , None)




def information():
    print("\n[+] PASSWORD BANK PVT. LTD. [+]")
    print("\nWe store all your passwords , Have a account Now for Free .")

def menu():
    print("\n[1] CREATE NEW ACCOUNT ")
    print("[2] LOGIN TO EXISTING ACCOUNT ")
    print("[3] EXIT ")


def new():

    j=1
    while j==1:

        holder_name = input(" \nEnter your name\n")
        holder_age = int(input("\nEnter your age\n"))
        if holder_name == ""  or holder_age == "":
            print("\n[+] Empty Records Must enter values [+]")



        else:
            j=j+1
    i=1
    while i==1:

        holder_password = input("\nEnter your password \n")
        holder_password_confirm = input ("\nConfirm your password \n")
        if holder_password != holder_password_confirm :
            print("Incorrect Password Matching . Try again ")

        else :
           

            #Accountnumber randomer
            lower="abcdefghijklmnopqrstuvwxyz"
            num="0123456789"

            unit=lower+num
            pwdlen=12

            holder_acc_id="".join(random.sample(unit,pwdlen))

            print("\nYour account number is :\n",holder_acc_id)
            
            i=i+1

            #Dta Upload

            upload = {
                "Account ID":holder_acc_id,
                "Name":holder_name,
                "Age":holder_age,
                "Password":holder_password_confirm

            }

            result = firebase.post("/password-database-df4db-default-rtdb/Account" , upload)
            
            print("\n Your Account Unique ID is (Always Remember it ) :")
            holder_unique_id = result.get("name")

            print("\nAccount creation success . Now you can login\n")

            filename= "acc_uid"+holder_acc_id+".txt"

            file = open(filename , "w+")
            file.write(holder_unique_id)

            login_req = input("\nDo you want to login ? (Y/N)\n")
            if login_req == "Y" or login_req == "y" :
                existing()

            elif login_req == "N" or login_req == "n" :
                break



def existing():
    requested_acc_id = input("\nEnter Your Account ID \n")
    requested_acc_pwd = input("\nEnter Your Password \n")
    requested_uid = input("\nAccount Unique Id file Path \n(eg. /file/acc_uid001122.txt)\n")

    save_file = open(requested_uid , "r")
    retrived_uid = save_file.read()

    r= firebase.get("/password-database-df4db-default-rtdb/Account",retrived_uid)
    retrived_acc_id = r.get("Account ID")
    retrived_pwd = r.get("Password")
    retrived_name = r.get("Name")

    if retrived_acc_id == requested_acc_id and retrived_pwd == requested_acc_pwd :
        print("\nWelcome ",retrived_name)
        submenu()

        while True :

            bash_log = int(input("\nEnter Your Choice : \n"))

            if bash_log == 4:
                new_passwd()

            elif bash_log == 5 :
                ret_pwd()

            elif bash_log == 6 :
                ddel_rec()

            else :
                print("Unknow Input")

        

    else :
        print("Sorry , Bad request . ")

def submenu():

    #Menu when account is logged in 
    print("\n[4] Save New Password\n[5] Retrieve all Passwords\n[6] Delete Records\n[7]Logout")

def new_passwd():

    app_name = input("\nApp Name\n")
    username_app = input("\nEnter Username\n")
    passwd_app =input("\nEnter Password\n")

    upload_pwd = {
                "App Name":app_name,
                "Username":username_app,
                "Password":passwd_app,

            }
    
    pwd_result = firebase.post("/password-database-df4db-default-rtdb/Passwords" , upload_pwd)
            
    print("\n Your Password Unique ID is (Always Remember it ) :")
    pwd_unique_id = pwd_result.get("name")

    print("\nData Sucessfully Updated\n")

    filename= "pwduid"+app_name+".txt"

    file = open(filename , "w+")
    file.write(pwd_unique_id)

def ret_pwd():
    requested_uid_pwd = input("\nAccount Unique Id file Path \n(eg. /file/acc_uid001122.txt)\n")

    save_file_pwd = open(requested_uid_pwd , "r")
    retrived_uid_pwd = save_file_pwd.read()

    re= firebase.get("/password-database-df4db-default-rtdb/Passwords",retrived_uid_pwd)
    retrived_username = re.get("Username")
    retrived_passwd = re.get("Password")

    print("Username : ",retrived_username)
    print("Password :",retrived_passwd)

def ddel_rec():
    print("Feature will Updated Soon ")















information()
menu()

while True :
    
    bash =int( input ("\nEnter Your Choice : \n"))

    if bash == 1:
        new()

    elif bash == 2 :
        existing()

    elif bash == 3 :
        print("Thanks for Using")

    else :
        print("Unknown Input")





