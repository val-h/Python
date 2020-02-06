line_of_numbers = input("Line of numbers: ")
arrNums = [int(x) for x in line_of_numbers.split()]
freq = {}
for i in arrNums:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

def MaxKeyValue(f):         # Fastest way of finding max key - value
    v = list(f.values())
    k = list(f.keys())
    return k[v.index(max(v))]

print(MaxKeyValue(freq))
    