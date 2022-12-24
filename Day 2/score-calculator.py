"""
Go through a sheet and calculate the score for rock, paper, scizzors. First
column is what your opponent will do, second is what you should do in response.
Win = 6 points
Draw = 3 points
Loss = 0 points
Rock is A & X, 1 point
Paper is B & Y, 2 points
Scizzors is C & Z, 3 points
"""
# Return points according to who won.
def determineWinner(opponent, you):
    win = 6
    draw = 3
    loss = 0
    # Opponent wins
    if ((opponent == "A" & you == "Z") or (opponent == "B" & you == "X") or
        (opponent == "C" & you == "Y")):
        return loss
    # You win
    elif ((you == "A" & opponent == "Z") or (you == "B" & opponent == "X") or
        (you == "C" & opponent == "Y")):
        return win
    elif (opponent == you):
        return draw


def calculatePoints(filename):
    tempPoints = []
    
    with open(filename) as file:
        for line in file:
            opp = line[0]
            you = line[1]
            tempScore = 0
            if(you == "X"):
                tempScore = 1
            elif(you == "Y"):
                tempScore = 2
            elif(you == "Z"):
                tempScore = 3
            tempScore += determineWinner(opp, you)
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