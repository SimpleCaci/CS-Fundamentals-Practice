inputList = [3, 5, 2, 3, 4, 6, 1, 3]

for i in range(1, len(inputList)):
    key = inputList[i]
    j = i - 1

    while j >= 0 and inputList[j] > key:
        inputList[j + 1] = inputList[j]
        j -= 1

    inputList[j + 1] = key

print(inputList)
