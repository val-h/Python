hour = int(input())
min = int(input())

min += 15
if min >= 60:
    min %= 60
    hour += 1
if hour == 24:
    hour = 0

if min < 10:
    print(f'{hour}:0{min}')
else:
    print(f'{hour}:{min}')