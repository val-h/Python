usrInp = input('Word to calculate: ').lower()
points = 0
for c in usrInp:
    if c == 'a':
        points += 1
    elif c == 'e':
        points += 2
    elif c == 'i':
        points += 3
    elif c == 'o':
        points += 4
    elif c == 'u':
        points += 5
print(points)