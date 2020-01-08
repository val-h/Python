import math

record = float(input())
meters = float(input())
mSec = float(input())

iTime = meters * mSec
delay = meters / 15
delay = math.floor(delay) * 12.5
iTime += delay

if iTime < record:
    print(f'Yes, he succeeded! the new world record is {iTime:.2f} seconds.')
else:
    print(f'No, he failed! He was {iTime - record:.2f} seconds slower.')