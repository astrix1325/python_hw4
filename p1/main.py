def increase_fail_count(current_cnt, limit=5):
    current_cnt += 1
    if current_cnt >= limit:
        print("Fail")
        exit()
    else:
        print("Try again")
    return current_cnt

correct_password = "Aerospace"
current_cnt = 0

while current_cnt < 5:
    password = input()
    if password == correct_password:
        print ("LOGIN")
        break
    else: 
        current_cnt = increase_fail_count(current_cnt,limit=5)
