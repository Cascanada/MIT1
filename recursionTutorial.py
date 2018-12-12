def factorialRecursive(n):
    # Base Case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n!= n! * (n-1)!
    else:
        return n * factorialRecursive(n-1)

# print(factorialRecursive(3))

def sumRecursiveLocal(currentNumber, accumulatedSum):
    # Base Case
    # Return the final state.
    if currentNumber == 11:
        return accumulatedSum

    # Recursive Case
    # Thread the state through the recursive call
    else:
        return sumRecursiveLocal(currentNumber + 1, accumulatedSum + currentNumber)

# print(sumRecursiveLocal(1,0))


#Global mutable state
currentNumber = 1
accumulatedSum = 0

def sumRecursiveGlobal():
    global currentNumber
    global accumulatedSum

    # Base case
    if currentNumber == 11:
        return accumulatedSum

    # Recursive case
    else:
        accumulatedSum = accumulatedSum + currentNumber
        currentNumber = currentNumber + 1
        return sumRecursiveGlobal()

#print(sumRecursiveGlobal())

