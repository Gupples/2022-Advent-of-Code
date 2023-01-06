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
    ranges = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            line = []
            this_range = []
            elf1 = row[0].split("-")
            elf2 = row[1].split("-")
            line.append(elf1[0])
            line.append(elf1[1])
            line.append(elf2[0])
            line.append(elf2[1])
            list.append(line)
            elf1_range = range(int(elf1[0]), int(elf1[1]) + 1)
            elf2_range = range(int(elf2[0]), int(elf2[1]) + 1)
            this_range.append(elf1_range)
            this_range.append(elf2_range)
            ranges.append(this_range)
    return list

def find_overlaps(pairs):
    overlap = 0
    i = 1
    same = 0
    for pair in pairs:
        first_min = pair[FIRST_MIN]
        first_max = pair[FIRST_MAX]
        second_min = pair[SECOND_MIN]
        second_max = pair[SECOND_MAX]
        if ((first_min > second_min and first_max <= second_max) or 
            (first_min < second_min and first_max >= second_max)):
            if (first_min == second_min and first_max == second_max):
                continue
            else:
                overlap += 1
        i += 1
    # print(f"same: {same}")
    return overlap

def main():
    pairs = read_assignments("Day 4/assignments.csv")
    overlap = find_overlaps(pairs)
    print(f"Elf assignments that totally overlap: {overlap}")

if __name__ == "__main__":
    main()