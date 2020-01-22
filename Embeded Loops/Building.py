row = int(input('Enter the value for colums: '))
col = int(input('Enter the value for rows: '))
for i in range(row, 0, -1):
    level = ''
    for q in range(0, col,):
        if i == row:
            level += f'L{i}{q} '
        elif i % 2 == 0:
            level += f'O{i}{q} '
        elif i % 2 != 0:
            level += f'A{i}{q} '
    print(level)
    