import re
lineOfWords = input('Line of words: ')
words = re.findall(r"[\w]+", lineOfWords)
lowerCase = []
upperCase = []
mixed = []

for w in words:
    if w.islower():
        lowerCase.append(w)
    elif w.isupper():
        upperCase.append(w)
    else:
        mixed.append(w)

print(f'Lower-case: {", ".join(lowerCase)}')
print(f'Mixed-case: {", ".join(mixed)}')
print(f'Upper-case: {", ".join(upperCase)}')
