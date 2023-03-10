"""
Wrong Answers: 218, 343, 512, 535
"""
# Part 1 Answer: 466
total = 0

with open("Day 4/assignments.txt") as file:
    for line in file:
        contents = line.split(",")
        elf1 = contents[0]
        elf2 = contents[1]
        elf1_start, elf1_stop = elf1.split("-")[0], elf1.split("-")[1]
        elf2_start, elf2_stop = elf2.split("-")[0], elf2.split("-")[1]
        elf1_range = range(int(elf1_start), int(elf1_stop) + 1)
        elf2_range = range(int(elf2_start), int(elf2_stop) + 1)

        counter = 0

        for item in range(int(elf1_start), int(elf1_stop) + 1):
            if item in range(int(elf2_start), int(elf2_stop) + 1):
                counter += 1
            if counter == len(elf1_range) or counter == len(elf2_range):
                total += 1
                break

print(total)