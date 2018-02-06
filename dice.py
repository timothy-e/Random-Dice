import math
import random

def roll_die(s):
    return random.randrange(s) + 1

def get_length(n):
    if n == 0:
        return 1
    else:
        return int(math.log10(n)) + 1

# max_space(L) returns the largest number of spaces taken up by an item in L
def max_space(L):
    m = 0
    for i in L:
        m = max(m, get_length(i))
    return m

def max_list(L):
    m = L[0]
    for i in L:
        m = max(m, i)
    return m

while (True):
    sides = int(input("How many sides are on the dice? "))
    num = int(input("How many dice? "))
    trials = int(input("How many trials? "))


    # init arrays
    rolls = []
    for i in range(0, sides):
        rolls.append(0)
    sums = []
    for i in range(num, num * sides + 1):
        sums.append(0)

    # run trials
    for i in range(0, trials):
        for j in range(0, num):
            rolls[roll_die(sides) - 1] += 1
        s = 0
        for j in range(num):
            s += roll_die(sides)
        sums[s - 1 - num] += 1

    print("\n\n")
    
    # print rolls
    max_roll_space = max_space(rolls)
    highest_freq = max_list(rolls)
    # graph
    for i in range(highest_freq, 0, -1):
        s = "      "
        for j in rolls:
            if j >= i:
                s = s + (" " * 3) + "#" + (" " * max_roll_space)
            else:
                s = s + (" " * (max_roll_space + 4))
        print(s)

    # table
    s = ""
    for i in range(0, sides):
        s = s + " | " + str(i + 1) + (" " * max_roll_space)
    print("Rolls " + s)
    s = ""
    for i in range(0, sides):
        s = s + " | " + str(rolls[i]) + (" " * (max_roll_space - get_length(rolls[i]) + get_length(i)))
    print("      " + s)

    # print sums
    max_sum_space = max_space(sums)
    highest_freq = max_list(sums)
    
    # table
    s = ""
    for i in range(num, num * sides + 1):
        s = s + " | " + str(i) + (" " * max_sum_space)
    print("\nSums  " + s)
    s = ""
    for i in range(num, num * sides + 1):
        s = s + " | " + str(sums[i - num]) + (" " * (max_sum_space - get_length(sums[i - num]) + get_length(i)))
    print("      " + s)

    
    # graph
    for i in range(0, highest_freq):
        s = "      "
        for j in sums:
            if j >= i:
                s = s + (" " * 3) + "#" + (" " * max_sum_space)
            else:
                s = s + (" " * (max_sum_space + 4))
        print(s)

