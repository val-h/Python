line_of_numbers = input('Line of numbers: ')
arr = [int(x) for x in line_of_numbers.split()]
middle = int(len(arr) / 2)
output = ''

if len(arr) == 1:
    output = arr[0]
elif len(arr) % 2 == 0:
    output = f'{arr[middle - 1]} {arr[middle]}'
else:
    output = f'{arr[middle - 1]} {arr[middle]} {arr[middle + 1]}'
print(output)

