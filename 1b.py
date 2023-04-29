filename = "inputs/1.txt"
lines = [0]
for l in open(filename):
    if l.rstrip():
        lines[-1] += int(l.rstrip())
    else:
        lines.append(0)
 
def main():
    return sum(sorted(lines)[-3:])

print(main())