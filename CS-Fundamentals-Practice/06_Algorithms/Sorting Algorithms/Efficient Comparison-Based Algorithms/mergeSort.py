inputList = [22,3,1,4,23,43,5,9,23]

#first I split
#then I sort
#then I merge

def split(ogList):
    if (len(ogList)==1):
        return ogList
    left = split(ogList[0:int(len(ogList)/2)])
    right = split(ogList[int(len(ogList)/2):len(ogList)])
    return [left, right]

print(split(inputList))