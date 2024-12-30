def readData(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

nums = []
def getNum(data):
    for l in data  :
        a = l[0]
        b = l[1]
        nums.append(a,b)

input = readData('input.txt')
getNum(input)
print(nums)