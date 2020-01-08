sqMetReq = int(input())

cost = float(sqMetReq * 7.61)
disc = cost * 0.18
finalCost = cost - disc

print(f'The final price is: {finalCost:.2f} lv.')
print(f'The discount is: {disc:.2f} lv.')