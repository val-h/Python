day = int(input('Number for day of the week: '))
weekDays = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
print(weekDays.get(day, 'Invalid day!'))    # Lots of new stuff learned