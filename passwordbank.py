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




information()
menu()
bash =int( input ("\nEnter Your Choice : \n"))

if bash == 1:
    new()

