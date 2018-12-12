# Marc notes on the disorganized handyman

# problem of n + (n-1) + (n-2) ... +1 = n(n+1)/2

def searchSpace(n):
    s=0
    for i in range(n+1):
        s += i
    print(s)

def seachSpaceSimple(n):
    s = (n*(n+1))/2
    print(s)

n=4
# searchSpace(100)
# seachSpaceSimple(100)

# Recursively compare one bolt to all the nuts, then split nuts into three groups.
# Once done, take the nut that fits (group three) and compare it to all bots!
# Now you have three groups (nuts and bolts bigger and smaller than the original set, and the matching set).
# This is called Pivoting!

import random

def disorganizedHandymanSetup(n):

    # Create the bag of nuts and bolts!
    bolts = []
    nuts = []
    for i in range(n):
        bolts.append('b'+str(i))
        nuts.append('n'+str(i))
    random.shuffle(bolts)
    random.shuffle(nuts)

    # Create Pairs Variable
    pairs = []

    # Call recursive function
    disorganizedHandymanExecution(bolts, nuts, pairs)

    # Print final result
    print(pairs)


def disorganizedHandymanExecution(bolts, nuts, pairs):
    # Exit condition
    if len(nuts) ==0:
        return pairs
    elif len(nuts) == 1:
        pairs.append([nuts[0], bolts[0]])
        return pairs

    # Recursive Condition
    # Setup local variables
    nutsSmaller = []
    nutsLarger = []
    boltsSmaller = []
    boltsLarger = []

    # Make a first pass with 1 bolt and corresponding nut!
    for i in nuts:
        if bolts[0][1:] == i[1:]:
            pairs.append([bolts[0], i])
        elif bolts[0][1:] > i[1:]:
            nutsSmaller.append(i)
        else:
            nutsLarger.append(i)
    del bolts[0]
    for i in bolts:
        if pairs[-1][-1][1:] > i[1:]:
            boltsSmaller.append(i)
        else:
            boltsLarger.append(i)
    nuts = nuts.remove(pairs[-1][-1])

    # Call recursively
    disorganizedHandymanExecution(boltsSmaller, nutsSmaller, pairs)
    disorganizedHandymanExecution(boltsLarger, nutsLarger, pairs)
    return pairs

disorganizedHandymanSetup(100)


