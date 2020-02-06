first_line_of_chars = input('First line: ')
second_line_of_chars = input('Second line: ')
fArr = first_line_of_chars.split()
sArr = second_line_of_chars.split()
output = ''

if fArr <= sArr:
    for i in fArr: output += i
    output += '\n'
    for i in sArr: output += i
else:
    for i in sArr: output += i
    output += '\n'
    for i in fArr: output += i

print(output)
