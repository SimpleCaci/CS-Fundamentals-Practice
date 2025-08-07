inputList = [22,3,1,4,23,43,5,9,3,23,24,511,323423,4,23]

#first I split
#then I sort
#then I merge

def splitAndMerge(ogList):
    if len(ogList) == 1:
        return ogList
    
    mid = len(ogList) // 2
    leftList = splitAndMerge(ogList[:mid])
    rightList = splitAndMerge(ogList[mid:])
    
    return sort(leftList, rightList)

def sort(leftList, rightList):
    sortedList = []

    while leftList and rightList:
        if leftList[0] < rightList[0]:
            sortedList.append(leftList.pop(0))
        else:
            sortedList.append(rightList.pop(0))

    sortedList += leftList
    sortedList += rightList

    return sortedList




print(splitAndMerge(inputList))