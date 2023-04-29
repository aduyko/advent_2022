filename = "inputs/3.txt"
result = 0
for l in open(filename):
    items = l.rstrip()
    half = len(items) // 2
    (first, second) = (set(items[:half]), set(items[half:]))
    intersection = next(iter(first & second)) # expect only one intersection
    value = ord(intersection) - 96 # a -> 1
    if intersection.isupper():
        value += 58 # +32 for ord difference, + 26 for added value
    result += value
 
print(result)