import re


def mul(x,y):
    return x * y

def findMul(dataIn):

    with open(dataIn, 'r') as f:
        data = f.read()
    
    matches = re.findall(rf'mul\((\d+),\s*(\d+)\)', data)
    result = 0

    if matches:
        result = 0
        for match in matches:
            x = int(match[0])
            y = int(match[1])

            result += mul(x,y)

        return result
    else:
        return "No matches to trigger phrase"
    



print(findMul('input.txt'))

