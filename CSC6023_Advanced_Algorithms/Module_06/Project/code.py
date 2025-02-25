"""
Nick Conant-Hiley
Merrimack College
Module 06 Project
"""
from math import log2
import  random

# ---------------My Function Algorithm--------------------
def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif ((log2(x) *5) % 23) < (x % 19):
        return (log2(x)* 2)**3
    else:
        return (log2(x)**2) - x

# -------------Hill Climb Algorithm-----------------------
def hillClimb(arr, start_index):

    if start_index < 0 or start_index >= len(arr):
        return None

    current_index = start_index


    while True:

        left = current_index - 1 if current_index > 0 else current_index
        right = current_index + 1 if current_index < len(arr) - 1 else current_index

        # Check to see if code is already at peak
        if arr[left] < arr[current_index] and arr[right] < arr[current_index]:
            return current_index, arr[current_index]

        # Shoulder Checks --------------------------------------
        # Shoulder check right
        while right < len(arr) and arr[right] == arr[current_index]:
            current_index = right
            right += 1

        # Shoulder check left
        while left > 0 and arr[left] == arr[current_index]:
            current_index = left
            left -= 1
        # Highest hill code ----------------------------------
        # Choose the higher path
        if right < len(arr) and left > 0 and arr[right] > arr[current_index] and arr[left] > arr[current_index]:
            if arr[right] > arr[left]:
                current_index = right
            else:
                current_index = left

        # check if in pit
        elif right < len(arr) and arr[right] > arr[current_index]:
            current_index = right

        elif left > 0 and arr[left] > arr[current_index]:
            current_index = left
        else:
            return current_index, arr[current_index]



def main():
    values = [myFunction(x) for x in range(1, 10_000)]
    global_max = max(values)
    best_local_max = float("-inf")
    k = 10

    for _ in range(k):
        rand_num = random.randint(1, 9998)
        local_max_index, local_max_value = hillClimb(values, rand_num)

        if local_max_value > best_local_max:
            best_local_max = local_max_value

    if best_local_max == global_max:
        print(f"After {k} tries, the greatest local max was {best_local_max} which was the global max")
    else:
        print(f"After {k} tries, the greatest local max discovered was {best_local_max}")
        print(f"The actual global max was {global_max}")


if __name__ == '__main__':
    main()









