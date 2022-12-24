"""
Go through a sheet and calculate the score for rock, paper, scizzors. First
column is what your opponent will do, second is what the round should end as.
Win = 6 points
Draw = 3 points
Loss = 0 points
Rock is A and 1 point
X is rock and loss.
Paper is B and 2 points
Y is paper and draw.
Scizzors is C and 3 points
Z is scizzors and win.
"""
# Return points according to who won.
def determinePoints(opponent, outcome):
    rock = 1
    paper = 2
    scizzors = 3
    # if opponent chooses rock
    if opponent == "A":
        if outcome == "X":
            return scizzors
        elif outcome == "Y":
            return rock
        elif outcome == "Z":
            return paper
    # if opponent chooses paper
    elif opponent == "B":
        if outcome == "X":
            return rock
        elif outcome == "Y":
            return paper
        elif outcome == "Z":
            return scizzors
    # if opponent chooses scizzors
    elif opponent == "C":
        if outcome == "X":
            return paper
        elif outcome == "Y":
            return scizzors
        elif outcome == "Z":
            return rock

def calculatePoints(filename):
    tempPoints = []
    
    with open(filename) as file:
        for line in file:
            opp = line[0]
            result = line[2]
            tempScore = 0
            if(result == "X"):
                tempScore = 1
            elif(result == "Y"):
                tempScore = 2
            elif(result == "Z"):
                tempScore = 3
            choice = (opp, result)
            tempPoints += choice
            tempPoints.append(tempScore)
    return tempPoints

def display(score):
    print(f"Your point total is {score}\n")

def main():
    points = []
    points = calculatePoints("Day 2/test-guide.txt")
    score = sum(points)
    display(score)
    

if __name__ == "__main__":
    main()