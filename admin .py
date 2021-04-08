import csv
import re
from cryptography.fernet import Fernet
from Crypto.Cipher import AES


user_name = input("Enter Username : ")

while True:
    pass_word = input("Enter Password : ")
    if len(pass_word) < 8:
        print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9A-Z(!@#$%^&*_)]',pass_word) is None:
        print("Make sure your password has a number,capital and symbols in it")
    else:
        print("Your password seems fine") 
        obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
        ciphertext = obj.encrypt(pass_word)
        pass_word_str = str(ciphertext)
        str = pass_word_str.split("'")[1].split("'")[0]
        print(str)
        print(type(pass_word_str))
        with open("login.csv","r") as login_file:
            login_read = csv.reader(login_file)
            for row in login_read:
                if row == []:
                    with open("login.csv","w") as login_file:
                        login_writer = csv.writer(login_file)
                        login_writer.writerow([f"{user_name}",f"{str}"])
                        print("Successful Register")
                        break
                else:
                    with open("login.csv","a") as login_file:
                        login_writer = csv.writer(login_file)
                        login_writer.writerow([f"{user_name}",f"{str}"])
                        print("Successful Register")
                        break
        break
lst =[]
with open("login.csv","r") as login_file:
    login_read = csv.reader(login_file)
    for row in login_read:
        lst.append(row[1])

mes_dec =lst[8]
print(mes_dec)
obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
DEC = obj2.decrypt(mes_dec)
print(DEC)
