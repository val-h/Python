name = input('Title: ')
books = int(input('How many books are there: '))
cnt = 0
while cnt < books:
    newBook = input()
    if newBook == name:
        break
    cnt += 1
if cnt < books:
    print(f'You checked {cnt} books and found it')
else:
    print('The book you search is not here!')
    print(f'You checked {cnt} books.')