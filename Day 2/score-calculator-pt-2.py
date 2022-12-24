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
def determineWinner(opponent, you):
    win = 6
    draw = 3
    loss = 0
    # Opponent wins
    if ((opponent == "A" and you == "Z") or (opponent == "B" and you == "X") or
        (opponent == "C" and you == "Y")):
        return loss
    # You win
    elif ((opponent == "A" and you == "Y") or (opponent == "B" and you == "Z")
        or (opponent == "C" and you == "X")):
        return win
    # Draw
    elif ((opponent == "A" and you == "X") or (opponent == "B" and you == "Y")
        or (opponent == "C" and you == "Z")):
                return draw


def calculatePoints(filename):
    tempPoints = []
    
    with open(filename) as file:
        for line in file:
            opp = line[0]
            you = line[2]
            tempScore = 0
            if(you == "X"):
                tempScore = 1
            elif(you == "Y"):
                tempScore = 2
            elif(you == "Z"):
                tempScore = 3
            outcome = determineWinner(opp, you)
            tempScore += outcome
            tempPoints.append(tempScore)
    return tempPoints

def display(score):
    print(f"Your point total is {score}\n")

def main():
    points = []
    points = calculatePoints("Day 2/guide.txt")
    score = sum(points)
    display(score)
    

if __name__ == "__main__":
    main()