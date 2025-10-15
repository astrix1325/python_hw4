CPWD = "Aerospace"
LIMIT = 5
current_cnt = 0

def increase_fail_count(current_cnt):
     return current_cnt + 1 

PWD = input("Password: ")

if PWD == CPWD:
    print("Login")
else: 
    while current_cnt < LIMIT:
        current_cnt = increase_fail_count(current_cnt)
        if current_cnt >= LIMIT:
            print("Failed")
            break 
        print ("Check again")
        PWD = input("Password: ")
        if PWD == CPWD:
            print("Login")
            break
