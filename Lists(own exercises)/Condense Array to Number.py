usrInp = input('Enter the array: ')
arr = [int(x) for x in usrInp.split()]
condensedArr = []

while len(arr) > 1:
    for i in range(0, len(arr) - 1):
        condensedArr.append(arr[i] + arr[i + 1])
    arr = condensedArr
    condensedArr = []
print(arr[0])
