# i don't really know how this works
n = int(input('Enter a value for n: '))
stop = False
cnt = 1
for i in range(1, n + 1):
    for q in range(0, i):
        print(str(cnt) + ' ', end='')
        if cnt == n:
            stop = True
            break
        cnt+=1
    print()
    if stop == True:
        break
