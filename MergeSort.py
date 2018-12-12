#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please

#mergeSort: Recursive Divide-and-Conquer algorithm.

#This procedure assumes left and right are sorted lists in ascending order,
#and merges them to produce a sorted list in ascending order.
#This procedure returns a new sorted list containing the same elements as L.
#L is not modified.

# Edited by Marc to be able to deal with len(list)s other than 2^n.

def mergeSort(L):

    if len(L) == 1:
        return [L[0]]
    elif len(L) == 2:
        if L[0] <= L[1]:
            return [L[0], L[1]]
        else:
            return [L[1], L[0]]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left, right)

def merge(left, right):

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def printMerge(M):
    print(M)


inp =[23, 3, 45, 7, 6, 11, 14, 12]
inp1 = [23, 3, 45, 7]
inp2 = [23, 3, 45, 7, 6, 11, 14, 12, 98]
inp3 = [7, 6, 5, 4, 3, 2, 1, 0]
print(mergeSort(inp))
print(mergeSort(inp1))
print(mergeSort(inp2))
print(mergeSort(inp3))

printMerge(mergeSort(inp3))
