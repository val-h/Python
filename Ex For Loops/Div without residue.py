n = int(input('Enter the number of elements: '))
l1, l2, l3 = 0, 0, 0
for i in range(1, n + 1):
    num = int(input(f'Enter a value for number {i}: '))
    if num % 2 == 0:
        l1 += 1
    if num % 3 == 0:
        l2 += 1
    if num % 4 == 0:
        l3 += 1
l1 = l1 / n * 100
l2 = l2 / n * 100
l3 = l3 / n * 100
print(f'Chart 1 = {l1:.2f}%')
print(f'Chart 2 = {l2:.2f}%')
print(f'Chart 3 = {l3:.2f}%')