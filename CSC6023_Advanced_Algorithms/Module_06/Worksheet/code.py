import random

def lasVegas(target, nums):
    tries = 1
    i = random.randint(0, len(nums) - 1)

    while nums[i] != target:
        tries += 1
        i = random.randint(0, len(nums) - 1)

    if nums[i] == target:
        return i, tries


def monteCarlo(target, nums, limit):
    tries = 1
    k = 1
    i = random.randint(0, len(nums) - 1)
    while nums[i] != target and k < limit:
        tries += 1
        k += 1
        i = random.randint(0, len(nums) - 1)

    if nums[i] == target:
        return i, tries
    else:
        return -1, tries

def generateRandom1and0(amount):
    half = amount // 2

    ones = [1] * half
    zeros = [0] * half

    arr = zeros + ones
    random.shuffle(arr)

    return arr


# ----------------------------------------------------------------------

amount = 10_000
rand_list  = generateRandom1and0(amount)
target = 1
indexLV , triesLV = lasVegas(1, rand_list)
print("--------------------Las Vegas Algorithm--------------------")
print(f"Target number: '{target}', found at index {indexLV}")
print(f"It took {triesLV} {'tries' if triesLV > 1 else 'try'}")

print("-------------------Monte Carlo Algorithm-------------------")
k = 10
indexMC, triesMC = monteCarlo(target, rand_list, k)
if indexMC == -1:
    print(f"Monte Carlo algorithm did not find {target} after {triesMC}")
else:
    print(f"Monte Carlo algorithm: Target '{target}' found at index {indexMC}")
    print(f"It took {triesMC} {'tries' if triesMC > 1 else 'try'}")



