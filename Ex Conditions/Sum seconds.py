p1 = int(input())
p2 = int(input())
p3 = int(input())

seconds = p1 + p2 + p3
min = int(seconds / 60)
seconds = seconds % 60

if  seconds < 10:
    print(f'{min}:0{seconds}')
else:
    print(f'{min}:{seconds}')