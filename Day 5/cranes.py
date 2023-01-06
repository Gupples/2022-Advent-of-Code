"""
Each puzzle has a diagram at the head of it with directions to
move crates from one stack to another. Crates are moved one at
a time. Find what crate is on the top of each stack after all
moves have been executed.
Strategy: Have each stack be an array with the letters in brackets
being the value. stacks.txt has 9 stacks, index values are:
[1], [5], [9], [13], [17], [21], [25], [29], [33].
Basically, for each stack, add 4.

When moving crates from one array to another, use x = array1.pop[0]
to store, and array2.insert(0, x) to deposit.
"""
# get info about the graph
def first_pass(file):
    pass

# process data
def second_pass(file):
    pass

def get_stacks_info():

    pass

def get_number_of_stacks(line):
    text = line.split()
    print(f"Text = {text}")

    return len(text)

def get_stacks(filename):
    # find out how many lines contain the stacks.
    stack_lines = 0
    # find out when instructions start.
    instructions_start = -1
    is_over = False
    with open(filename) as file:

        # Search for end of diagram. To do so, search for the
        # label line, using the lable for stack 1.
        for text in file:
            line = text.split(" ")
            if line[0] != "\n":
                if line[0] != "move" and line[1] == "1":
                    index_line = text
                    is_over = True
                    instructions_start = stack_lines + 3
            if is_over == False:
                stack_lines += 1
        print(stack_lines)
        # Now that we have the grid, we need to find out how many 
        # stacks there are.
        # VVV debug code for confirming correct line VVV
        # print(index_line)
        stacks_length = get_number_of_stacks(index_line)
        print(f"Number of stacks: {stacks_length}")
        # Create array of lists
        stacks = []
        print(stacks)


    pass


def main():
    get_stacks("Day 5/test-stacks.txt")
    pass

if __name__ == "__main__":
    main()