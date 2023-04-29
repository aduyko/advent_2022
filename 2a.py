filename = "inputs/2.txt"
score = 0
score_mapping = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

for l in open(filename):
    score += score_mapping[l.rstrip()]
 
print(score)