import csv
import stdiomask

def login():
    user_name = input("Enter Username : ")
    pass_word = stdiomask.getpass()
    with open("login.csv") as login_check:
        login_read = csv.reader(login_check)
        for row in login_read:
            while True:
                if user_name == row[0] and pass_word== row[1]:
                    result = exam()
                    save_result(user_name,pass_word,result)
                    break
                elif user_name != row[0]:
                    print("Please ask administrator for registration.")
                    break
                elif pass_word != row[1]:
                    print("Wrong Password. Please enter correct password.")
                    pass_word = stdiomask.getpass()



def exam():
    user_result = 0
    with open("que.csv")as file:
        with open("mcq.csv") as mcq:
            mcq_read = csv.reader(mcq)
            que_read = csv.reader(file)
            i = 1
            for que_row,mcq_row in zip(que_read,mcq_read):
                
                print(f"\nQuestion {i}:{que_row[1]}")
                print(f'''A:{str(mcq_row[1].split(":")[1])}\t\t\t\tB:{str(mcq_row[2].split(":")[1])}
C:{str(mcq_row[3].split(":")[1])}\t\t\t\tD:{str(mcq_row[4].split(":")[1])}''')

                i+=1
                user_ans = input("Enter Your Ans : ").upper()


                for single_item in mcq_row:
                    near_ans= single_item.startswith("[")
                    if near_ans == True:
                        real_ans=single_item.split("[")[1].split("]")[0]
                
                if real_ans==user_ans:
                    user_result +=1
    return user_result
                
def save_result(user_name,pass_word,user_result):
    with open("result.csv","w") as result:
        result_write = csv.writer(result)
        result_write.writerow([f"{user_name},{pass_word},{(user_result*100)/10}%"])
    print(f"Your Result is {(user_result*100)/10}%")        

if __name__ == "__main__":

    login()