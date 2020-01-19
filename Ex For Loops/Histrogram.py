n = int(input('Number of elements: '))
p1, p2, p3, p4, p5 = 0.0, 0.0, 0.0, 0.0, 0.0 # first time trying this
for i in range(1, n + 1):
    num = int(input(f'Value for index {i}: '))
    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1
print(f'P1 = {p1 / n * 100:.2f}%')
print(f'P2 = {p2 / n * 100:.2f}%')
print(f'P3 = {p3 / n * 100:.2f}%')
print(f'P4 = {p4 / n * 100:.2f}%')
print(f'P5 = {p5 / n * 100:.2f}%')