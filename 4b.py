filename = "inputs/4.txt"
result = 0
for l in open(filename):
    (first, second) = [range(int(i.split("-")[0]), int(i.split("-")[1])+1) for i in l.rstrip().split(",")]

    if (set(first).intersection(second)):
        result += 1
 
print(result)