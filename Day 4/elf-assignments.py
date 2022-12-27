"""
Each line is a pair of elves, each elf having an assignment. Find out how many
pairs that have one elf completely covering the other's assignment (eg. 
6-6, 4-6; 2-8,3-7; etc.)
Strategy:
Read csv files, have each value equal
"""
import csv

FIRST_MIN = 0
FIRST_MAX = 1
SECOND_MIN = 2
SECOND_MAX = 3

def read_assignments(filename):
    list = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            line = []
            elf1 = row[0].split("-")
            elf2 = row[1].split("-")
            line.append(elf1[0])
            line.append(elf1[1])
            line.append(elf2[0])
            line.append(elf2[1])
            list.append(line)
    return list

def find_overlaps(pairs):
    overlap = 0
    for pair in pairs:
        first_min = pair[FIRST_MIN]
        first_max = pair[FIRST_MAX]
        second_min = pair[SECOND_MIN]
        second_max = pair[SECOND_MAX]
        if ((first_min >= second_min and first_max <= second_max) or 
            (first_min <= second_min and first_max >= second_max)):
            overlap +=  1
    return overlap

def main():
    pairs = read_assignments("Day 4/test-assignments.csv")
    overlap = find_overlaps(pairs)
    print(f"Elf assignments that totally overlap: {overlap}")

if __name__ == "__main__":
    main()