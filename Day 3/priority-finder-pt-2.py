"""
Each line is a rucksack, divided in two exactly down the middle. Find the item
in common between the two halves, and find the priority total of them all. 
Items are case-sensitive. a-z have priorities 1-26, and items A-Z have 
priorities 27-52.
Strategy: Find the priorities of each line and 
"""
# Get a list of common items in each rucksack
# Returns a list of common items.
def getItems(filename):
    # global within function
    items = []
    with open(filename) as file:
        for line in file:
            # items already used for sack.
            usedItems = []
            pocket1 = line[:len(line) // 2]
            # use .strip() for new line.
            pocket2 = line[len(line) // 2:].strip()
            commonItem = ""
            for item in pocket1:
                if item in pocket2:
                    commonItem = item
                    # can't use items, or you ignore the same item if it comes
                    # in a later sack.
                    if commonItem not in usedItems:
                        usedItems.append(commonItem)
                        items.append(commonItem)
    return items


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
    items = getItems("Day 3/items.txt")
    # get the total scores of common items
    score = getScores(items)
    # display common scores
    print(f"The total score of priority items is {score}")

if __name__ == "__main__":
    main()