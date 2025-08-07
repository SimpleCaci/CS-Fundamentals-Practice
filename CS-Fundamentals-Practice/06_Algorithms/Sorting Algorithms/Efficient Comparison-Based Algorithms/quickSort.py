import random

ogList = [3, 3, 23,3,3,3,3,43534,32,34,23,42,34,23,4,23,42,5,36,4,56,685,5,75,67,89,69,78,56,3,5,34,53,45,345,34,53,45,345,45, 2, 34, 23, 5, 34, 345, 6, 7, 623, 34, 2, 35, 6]

def quickSortStepping(ogList):
    leftList = []
    rightList = []
    pivot = random.choice(ogList)
    for item in ogList:
        if item < pivot:
            leftList.append(item)
        elif item > pivot:
            rightList.append(item)
        # skip == pivot here for simplicity
    return leftList + [pivot] + rightList

# Nesting the function 10 times
current = ogList
for i in range(10):
    current = quickSortStepping(current)
    print(f"Step {i+1}: {current}")

print("\nFinal result:", current)
