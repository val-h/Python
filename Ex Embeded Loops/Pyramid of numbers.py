# Now i know how it works 
n = int(input("Enter a value for n: "))
cnt = 1
stop = False
for row in range(1, n + 1):
    for col in range(0, row):
        print(str(cnt), end= ' ')
        if cnt == n:
            stop = True
            break
        cnt += 1
    if stop == True:
        break
    print()
