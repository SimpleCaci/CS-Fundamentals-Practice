#bubbleSort.py
numList = [3, 2, 1, 4, 5]
isSorted = False
while (not isSorted):
    isSorted = True
    for i in range(len(numList)-1):
       if numList[i] > numList[i+1]:
           temp = numList[i]
           numList[i] = numList[i+1]
           numList[i+1] = temp
           isSorted = False
       
print(numList)