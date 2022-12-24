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
def calculatePoints(filename):
    with open(filename) as file:
        for line in file:
            pass

def display(score):
    print(f"Your point total is {score}\n")

def main():
    points = []
    calculatePoints("test-guide.txt")
    score = sum(points)
    display(score)
    

if __name__ == "__main__":
    main()