"""
Each elf in elves.csv is represented by a space between a set of calories. Find
the elf that has the largest calorie count and enter the total calories that
elf has. 
Strategy; Go through line by line. Run a total, and if the line is an empty
space, reset the count.
"""
import csv

"""
find_most_calories - reads a list of values and returns the highest value.
"""
def find_most_calories(list):
    highest = 0
    for line in list:
        if line > highest:
            highest = line
    return highest
    
"""
get_calories - Reads a csv file and converts it into a list.
    Parameters: 
        filename: name of the file to be read
    Returns:
        calorie_list: the completed list with the total calories each elf is
            carrying.
"""
def get_calories(filename):
    calorie_list = []
    elf = 1
    with open(filename) as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            if row == "":
                elf += 1
                calorie_list.append(total)
                total = 0
            else:
                total += int(row)
    return calorie_list

def main():
    calories = get_calories("elves.csv")
    answer = find_most_calories(calories)
    print(f"The elf carrying the most calories is carrying {answer} "
        "calories.\n")

if __name__ == "__main__":
    main()