#   Begining to learn Lists
#
#   SOURCE: W3Schools - Python lists
#
#   There are four collection data types in the Python programming language:
#       - List is a collection which is ordered and changeable. Allows duplicate members.
#       - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#       - Set is a collection which is unordered and unindexed. No duplicate members.
#       - Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#

# Declaring the lists: name = ['index 0', 'index 1', ...]     lists are writen with square brackets.
firstEverCollection = ['apple', 'banana', 'cherry', "orange", "kiwi", "melon", "mango"] # the types of quotes dont matter 

# Calling the whole list - ['apple', 'banana', 'cherry']
print(firstEverCollection)

# Calling a specific element through its index - banana
print(firstEverCollection[1])

# Calling the last element(reverse stuff, definetly sueful) - cherry - aka Negative indexing
print(firstEverCollection[-1])

# Starts at index 2(included) and ends at index 5(not included) - aka Range of indexes
print(firstEverCollection[2:5])     # Could also be writen like - [:5] to 5th index or [2:] to last 

# Range of negative indexes
print(firstEverCollection[-4:-1])   # start( -4 ) included and end ( -1 ) not included: -4 < -1

# Changing the value of a specific item, refering to the index number
firstEverCollection[1] = 'blackcurrant'
print(firstEverCollection)

print('-------------------------------------------------------------')

# Loop through a list - quite simple
for i in firstEverCollection:
    print(f'' + i)

# Checking for item in the list
if 'apple' in firstEverCollection:
    print(f'Yes, apple is in the fruit list!')

# List lenght
print('List lenght:',len(firstEverCollection))

print('-------------------------------------------------------------')

# Adding items - using append()
firstEverCollection.append('pineapple')
print(firstEverCollection)

# Adding item to a specific index - insert()
firstEverCollection.insert(1, 'tomato')
print(firstEverCollection)

# Removing an item - remove()
firstEverCollection.remove('mango')
print(firstEverCollection)

# Removing at a specific index - pop()  
firstEverCollection.pop(1)      # if no index is provided it removes the last item

# del keyword - removes a specific index or the whole list
del firstEverCollection[0]
print(firstEverCollection)
del firstEverCollection
#   print(firstEverCollection) - This would give an error: name 'firstEverCollection' is not defined

# The clear() method ... well... it cleares the list ( :
firstEverCollection = ['apple', 'banana', 'cherry']
firstEverCollection.clear()
print(firstEverCollection)

print('-------------------------------------------------------------')

# Copying a list
original = [1337, 55, 619]
copyOfOriginal = original.copy()    # If copy() is not used copyOfOriginal will only be a
print(copyOfOriginal)               # reference/pointer to copy and changes to it will not apply

# Or use method list()
copyOfOriginalV2 = list(original)   # Still works
print(copyOfOriginalV2)

# Joining two lists using the + operator
letters = ['a', 'b', 'c']
digits = [5, 6, 7]

combination = letters + digits      # Concatenation for lists 
print(combination)                  # Or use the extend() method - works the same way

# Assigning a value to lists using for loop - append() method
for i in digits:                    # Going through each of digits indexes
    letters.append(i)               # Adding the value of index 'i' to the list letters

# List constructor - using list()
finalList = list(('pencil', 'pen', 'marker'))
print(finalList)
