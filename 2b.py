filename = "inputs/2.txt"
score = 0
score_mapping = {
    "A X": 3,
    "B X": 1,
    "C X": 2,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "A Z": 8,
    "B Z": 9,
    "C Z": 7,
}

for l in open(filename):
    score += score_mapping[l.rstrip()]
 
print(score)