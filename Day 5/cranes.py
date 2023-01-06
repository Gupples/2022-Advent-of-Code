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
def get_stacks(filename):
    # find out how many lines contain the stacks.
    # starting at -1 will give 0 index of label line
    stack_lines = -1
    is_over = False
    with open(filename) as file:
        # search for the label for stack 1.
        for line in file:
            if line[1] == "1":
                is_over = True
            if is_over == False:
                stack_lines += 1
        


    pass


def main():
    get_stacks("Day 5/test-stacks.txt")
    pass

if __name__ == "__main__":
    main()