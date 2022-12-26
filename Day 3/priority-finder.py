"""
Each line is a rucksack, divided in two exactly down the middle. Find the item
in common between the two halves, and find the priority total of them all. 
Items are case-sensitive. a-z have priorities 1-26, and items A-Z have 
priorities 27-52.
Strategy: Find the priorities of each line and 
"""
# Get a list of common items in each rucksack
# Returns a list of lists of common items.
def getItems(filename):
    # global within function
    commonItems = []
    with open(filename) as file:
        for line in file:
            # reset the list of common items
            items = []
            # reset the list of used items
            usedItems = []
            # Walk through each letter in the line
            for letter in line:
                # If it's not in the used letter index,
                if letter not in usedItems:
                    # add it.
                    usedItems.append(letter)
                # otherwise, it's a repeat item.
                else:
                    # if it's not already in the list of candidates,
                    if letter not in items:
                        # add it.
                        items.append(letter)
            commonItems.append(items)
    return commonItems

# Find the highest priority item in each rucksack. 
# Returns a list of items with highest priority.
def findItem(items):
    pass

# calculate the total score for each priority item.
# Returns the total score of each item's value.
def getScores(items):
    pass

def main():
    items = getItems("Day 3/test-items.txt")
    priorityItems = findItem(items)
    score = getScores(priorityItems)
    print(f"The total score of priority items is {score}")

if __name__ == "__main__":
    main()