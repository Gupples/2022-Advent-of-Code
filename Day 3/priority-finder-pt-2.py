"""
Each line is a rucksack. Find the item in common between groups of 3 sacks,
and find the priority total of them all. 
Items are case-sensitive. a-z have priorities 1-26, and items A-Z have 
priorities 27-52.

"""
# Get a list of common items in each rucksack
# Returns a list of common items.
def getGroups(filename):
    groups = []
    usedItems = []
    commonItem = ""
    elf1 = []
    elf2 = []
    i = 1
    with open(filename) as file:
        for line in file:
            if (i % 3 == 0):
                i += 1
                for item in line:
                    if item in elf1 and item in elf2:
                        commonItem = item
                        groups.append(commonItem)
                        break
            else:
                if (i % 3 == 1):
                    elf1 = line
                else:
                    elf2 = line
                i += 1
                
        
        pass
    return groups


# calculate the total score for each priority item.
# Returns the total score of each item's value.
def getScores(items):
    totalScore = 0
    for item in items:
        score = 0
        if item.islower():
            score = ord(item) - 96
        else:
            # uppercase items get an additional 26 points
            score = ord(item) - 64 + 26
        totalScore += score
    return totalScore

def main():
    # Find common items in the pockets
    items = getGroups("Day 3/test-items.txt")
    # get the total scores of common items
    score = getScores(items)
    # display common scores
    print(f"The total score of groups is {score}")

if __name__ == "__main__":
    main()