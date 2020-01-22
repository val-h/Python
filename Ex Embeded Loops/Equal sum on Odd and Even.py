start = int(input('Enter a start number: '))
finish = int(input('Enter a finish number: '))
for num in range(start, finish + 1):
    numToStr = str(num)
    oddSum = 0
    evenSum = 0
    for i, dig in enumerate(numToStr):
        if i % 2 == 0:
            evenSum += int(dig)
        else:
            oddSum += int(dig)
    if evenSum == oddSum:
        print(num)
