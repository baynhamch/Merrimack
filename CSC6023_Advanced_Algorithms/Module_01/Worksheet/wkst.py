"""
Nick Conant-Hiley
Merrimack College
Module 1 Worksheet problem #1
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

def MCSS(a):
    largest = 0
    for i in range(len(a)):
        acc = 0
        for j in range(i, len(a)):
            acc += a[j]
            if (acc > largest):
                largest = acc
    #returns largest contiguous subsequence value
    return largest


rn_arr = gen_random_num(-1000, 1000, 1000)

print("Maximum Value:", MCSS(rn_arr))
print("Array Length:", len(rn_arr))
print("Array:", rn_arr)

