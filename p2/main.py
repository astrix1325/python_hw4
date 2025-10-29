N = int(input())
cnt_3 = 0
while N != 0:
    if N % 10 == 3:
        cnt_3 += 1
    N = N // 10
print(cnt_3)
