#comparisonSort.py

inputList = [5,3,6,3,1,4]

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

for i in range(len(inputList)-1):
    smallest = inputList[i]
    smallestIndex = i
    for j in range(i, len(inputList)):
        if inputList[j] < smallest:
            smallest = inputList[j]
            smallestIndex = j
    temp = inputList[i]
    inputList[i] = inputList[smallestIndex]
    inputList[smallestIndex] = temp
    print(inputList)

print(inputList)