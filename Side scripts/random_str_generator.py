from random import randint

for x in range(50):
    num = randint(33, 127)
    print(chr(num), num)

def pass_generator(lenght):
    pass_str = u''
    for i in range(lenght + 1):
        pass_str += chr(randint(33, 127))
    return pass_str

pswd = pass_generator(12)
print(pswd)
