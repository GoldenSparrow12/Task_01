import csv
import stdiomask
import re

class Student:
    def __init__(self):
        self.login()

    def login(self):
        
        row_name= []
        row_pass = []
        user_num = 0

        with open("login.csv") as login_check:
            login_read = csv.reader(login_check)
            for row in login_read:
                row_name.append(row[0])
                row_pass.append(row[1])


            user_name = input("Enter Username : ")
            if user_name not in row_name:
                print("Please ask administrator for registration.")

            else:
                for i in range(len(row_name)):
                    if user_name == row_name[i]:
                        user_num = i
                pass_word = stdiomask.getpass()
                while True:
                    if pass_word not in row_pass[user_num]:
                        print("Wrong Password. Please enter correct password.")
                        pass_word = stdiomask.getpass()
                    
                    elif pass_word in row_pass[user_num]:
                        result= self.exam()
                        self.save_result(user_name,pass_word,result)
                        break
                   
    def exam(self):
        user_result = 0
        k=0
        with open("que.csv")as file:
            with open("mcq.csv") as mcq:
                mcq_read = csv.reader(mcq)
                que_read = csv.reader(file)
                que_no = 1
                for que_row,mcq_row in zip(que_read,mcq_read):
                    
                    print(f"\nQuestion {que_no}:{que_row[1]}")
                    print(f'''A:{str(mcq_row[1].split(":")[1])}\t\t\t\tB:{str(mcq_row[2].split(":")[1])}
C:{str(mcq_row[3].split(":")[1])}\t\t\t\tD:{str(mcq_row[4].split(":")[1])}''')

                    que_no+=1
                    k+=1
                    k1 = str(k)
                    same_que = 0
                    with open("mcq.csv") as mcq1:
                        mcq_read1 = csv.reader(mcq1)
                        for mcq_row_1 in mcq_read1:    
                            for i_name in mcq_row_1:
                                if i_name==k1:
                                    for j_name in mcq_row_1:
                                        if j_name.startswith("[") is True:
                                            same_que +=1

                    if same_que == 1: 
                        con = True
                        while con:
                            user_ans = input("Enter Your Ans : ").upper()
                            if user_ans in ["A","B","C","D"]:
                                con = False
                            else:
                                print("Enter In Between A-D")

                                
                            
                        for single_item in mcq_row:
                            near_ans= single_item.startswith("[")
                            if near_ans == True:
                                real_ans=single_item.split("[")[1].split("]")[0]
                        
                        if real_ans==user_ans:
                            user_result +=1

                    else:
                        user_ans = input("Enter Your Ans : ").upper()
                    try:
                        user_ans_1 = user_ans.split(" ")[0]
                        user_ans_2 = user_ans.split(" ")[1]
                    
                    except IndexError:
                        pass
                        
                    with open("mcq.csv","r") as file:    
                        read = csv.reader(file)

                        for mcq_rows in read:
                            _que = []
                            for single_item in mcq_rows:
                                near_ans= single_item.startswith("[")
                                if near_ans == True:
                                    real_ans=single_item.split("[")[1].split("]")[0]
                                    _que.append(real_ans)
                            if len(user_ans) == 3:
                                if user_ans_1 in _que and user_ans_2 in _que:
                                    user_result +=1
                                    break

        return user_result
                    
    def save_result(self,user_name,pass_word,user_result):
        with open("result.csv","w") as result:
            result_write = csv.writer(result)
            result_write.writerow([f"{user_name},{pass_word},{(user_result*100)/10}%"])
        print(f"Your Result is {(user_result*100)/10}%")  


class Admin:

    def __init__(self):
        while True:
            user_name = input("Enter Username : ")
            user_row= []
            with open ("login.csv") as file:
                read = csv.reader(file)
                for row in read:
                    user_row.append(row[0])

                if user_name in user_row:
                    print("User Already Exists")

                else:
                    while True:
                        pass_word = input("Enter Password : ")
                        if len(pass_word) < 8:
                            print("Make sure your password is at lest 8 letters")
                        elif re.search('[0-9]',pass_word) is None:
                            print("Make sure your password has a number,capital and special symbol in it")
                        elif re.search('[A-Z]',pass_word) is None: 
                            print("Make sure your password has a number,capital and special symbol in it")
                        elif re.search('[(!@#$%^&*_)]',pass_word) is None:
                            print("Make sure your password has a number,capital and special symbol in it")
                        else:
                            print("Your password seems fine")   

                            with open("login.csv","r") as login_file:
                                login_read = csv.reader(login_file)
                                for row in login_read:
                                    if row == []:
                                        with open("login.csv","w") as login_file:
                                            login_writer = csv.writer(login_file)
                                            login_writer.writerow([f"{user_name}",f"{pass_word}"])
                                            print("Successful Register")
                                            break
                                    else:
                                        with open("login.csv","a") as login_file:
                                            login_writer = csv.writer(login_file)
                                            login_writer.writerow([f"{user_name}",f"{pass_word}"])
                                            print("Successful Register")
                                            break
                            break
                    break
                

if __name__ == "__main__":


    ext = True
    while ext:
        try:
            input_select = int(input('''\nSelect 1 or 2 or 3
            1.Admin
            2.Student
            3.Exit\n'''))

            while True:    
                if input_select == 1:
                    a1 = Admin()
                    break
                elif input_select == 2:
                    s1 = Student()
                    break
                elif input_select == 3:
                    ext = False
                    exit()
                elif input_select not in [1,2,3]:
                    print("Enter 1 or 2 or 3")
                    input_select = int(input())
        
        except ValueError as e:
            print("Enter only number")

