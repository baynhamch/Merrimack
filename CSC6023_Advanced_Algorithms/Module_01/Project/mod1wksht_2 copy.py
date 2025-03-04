"""
Nick Conant-Hiley
Merrimack College
Module 1 Worksheet problem #2
01/16/25
"""
import random

# function to generate random numbers
# params are start: lowest possible value
# stop: Highest possible value for range
# amount: length of array for numbers generated
def gen_random_num(start, stop, amount):
    rand_num_array = []
    for i in range(amount):
        rand = random.randint(start, stop)
        rand_num_array.append(rand)
    return rand_num_array

# function to get maximum contiguous subsequence sum
# params are a: array function searches over
# function modified to print first and last index positions
def MCSS(a):
    largest = 0
    start_index = 0
    final_index = 0
    # empty array to collect elements summed from array
    final_values = []
    for i in range(len(a)):
        # temp_values holds the running amount
        temp_values = []
        acc = 0
        for j in range(i, len(a)):
            acc += a[j]
            # add specific elemnt in a array to temp values
            temp_values.append(a[j])
            if (acc > largest):
                largest = acc
                # 2 variables capture first and last positions
                # of index the program is summing
                start_index = i
                final_index = j
                final_values = temp_values.copy()
    # print statments for starting and final index positions
    # as well as elements that are being added together
    print("Index Start", start_index)
    print("Index End", final_index)
    print("Values for maximum:", final_values)
    # returns sum of contiguous subsequence
    return largest


rn_arr = gen_random_num(-1000, 1000, 1000)

print("Maximum Value", MCSS(rn_arr))
print("Array Length", len(rn_arr))
print("Array:", rn_arr)


