animal = input().lower()
if animal == 'dog':
    print('mammal')
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake' or animal == 'zucc':
    print('reptile')
else:
    print('unknown')