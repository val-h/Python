string_of_nums = input('Enter the string of numbers: ')
list_of_nums = string_of_nums.split()
for i in list_of_nums:
    if float(i) > 0:
        print(f'{i} => {round(float(i))}')
    else:
        print(f'{i} => {round(float(i))}')
# This is alot simpler in python
