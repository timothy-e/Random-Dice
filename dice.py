import math
import random

sides = int(input("How many sides are on the dice? "))
num = int(input("How many dice? "))
trials = int(input("How many trials? "))

def roll_die(s):
    return random.randrange(s) + 1

def get_length(n):
    if n == 0:
        return 1
    else:
        return int(math.log10(n)) + 1

def max_from_list(L):
    m = 0
    for i in L:
        m = max(m, get_length(i))
    return m

# init arrays
rolls = []
for i in range(0, sides):
    rolls.append(0)
sums = []
for i in range(num, num * sides + 1):
    sums.append(0)

# run trials
for i in range(0, trials):
    rolls[roll_die(sides) - 1] += 1
    s = 0
    for i in range(num):
        s += roll_die(sides)
    sums[s - 1 - num] += 1


# print rolls
max_rolls = max_from_list(rolls)
s = ""
for i in range(0, sides):
    s = s + " | " + str(i + 1) + (" " * max_rolls)
print("\nRolls " + s)
s = ""
for i in range(0, sides):
    s = s + " | " + str(rolls[i]) + (" " * (max_rolls - get_length(rolls[i]) + get_length(i)))
print("      " + s)

# print sums
max_sums = max_from_list(sums)
s = ""
for i in range(num, num * sides + 1):
    s = s + " | " + str(i) + (" " * max_sums)
print("\nSums  " + s)
s = ""
for i in range(num, num * sides + 1):
    s = s + " | " + str(sums[i - num]) + (" " * (max_sums - get_length(sums[i - num]) + get_length(i)))
print("      " + s)
