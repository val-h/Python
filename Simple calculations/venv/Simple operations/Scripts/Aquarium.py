lenght = int(input())
width = int(input())
height = int(input())
percTaken = float(input())

volume = lenght * width * height
ltVolume = volume * 0.001 #dividing by 10 for every cm input(3 times) to get the correct dm
freeVolume = ltVolume * (1 - (percTaken * 0.01))  #subtracting the percentages taken from the other parts

print(f'{freeVolume:.3f}')