n = int(input('Numbers to calculate: '))
sum = 0
for i in range(0, n):
    num = int(input(f'Number {i + 1}: '))
    sum += num
print(f'Sum = {sum}')