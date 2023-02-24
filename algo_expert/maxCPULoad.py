# your code goes here
class Endpoint:
    def __init__(self, s, l, isStart):
        self.start, self.load, self.isStart = s, l, isStart

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        return self.isStart == True and other.isStart == False

    def __repr__(self):
        return str(self.start) + " " + str(self.load) + str(self.isStart)


def maxCPULoad(arr):
    newArr = []
    for start, end, load in arr:
        newArr.append(Endpoint(start, load, True))
        newArr.append(Endpoint(end, load, False))
    newArr.sort()
    print(newArr)
    count, result = 0, 0
    for i in range(len(newArr)):
        if newArr[i].isStart:
            count += newArr[i].load
            result = max(result, count)
        else:
            count -= newArr[i].load
    return result
