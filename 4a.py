filename = "inputs/4.txt"
result = 0
for l in open(filename):
    (first, second) = [list(map(lambda x: int(x), i.split("-"))) for i in l.rstrip().split(",")]

    if (
        (first[0] >= second[0] and first[0] <= second[1]
         and first[1] >= second[0] and first[1] <= second[1]) or
        (second[0] >= first[0] and second[0] <= first[1]
         and second[1] >= first[0] and second[1] <= first[1])
    ):
        result += 1
 
print(result)