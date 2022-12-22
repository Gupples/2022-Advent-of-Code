"""
Each elf in elves.csv is represented by a space between a set of calories. Find
the elf that has the largest calorie count and enter the total calories that
elf has. 
Strategy; Go through line by line. Run a total, and if the line is an empty
space, reset the count.
"""
  
"""
get_calories - Reads a csv file and converts it into a list.
    Parameters: 
        filename: name of the file to be read
    Returns:
        calorie_list: the completed list with the total calories each elf is
            carrying.
"""
def get_calories(filename):
    # make a list of total calories
    calorie_list = []
    # open elves file
    with open(filename) as file:
        # start initial calorie count
        total = 0
        for line in file:
            # add calories
            total += int(line)
            # if this is the last thing the elf is carrying...
            if file.next() == "":
                # add the total to the list of calories and reset count.
                calorie_list.append(total)
                total = 0
        # The last elf won't have an empty line, so no file.next() trigger.
        # Add that manually.
        calorie_list.append(total)
    # return the finished list.
    return calorie_list
        

def main():
    # get the list of calories carried by each elf
    calories = get_calories("Puzzle 1/test_elves.txt")
    # Determine which count is highest.
    answer = calories[max]
    print(f"The elf carrying the most calories is carrying {answer} "
        "calories.\n")

if __name__ == "__main__":
    main()