filename = "inputs/3.txt"
result = 0
group = []
for l in open(filename):
    group.append(set(l.rstrip()))
    if len(group) == 3:
        intersection = next(iter(group[0] & group[1] & group[2]))
        value = ord(intersection) - 96
        if intersection.isupper():
            value += 58 # +32 for ord difference, + 26 for added value
        result += value
        group = []
 
print(result)