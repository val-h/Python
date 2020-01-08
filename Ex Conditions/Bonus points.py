num = int(input())
bonusPoints = 0

if num <= 100:
    bonusPoints += 5
elif 100 < num <= 1000:
    bonusPoints += num * 0.2
elif num > 1000:
    bonusPoints += num * 0.1

if num % 2 == 0:
    bonusPoints += 1
elif num % 10 == 5:
    bonusPoints += 2

print(bonusPoints)
print(bonusPoints + num)