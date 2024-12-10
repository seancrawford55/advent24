import re

def readData(file):
    data = str
    with open(file, 'r') as f:
        data = f.read()
    return data


def thereIsNoTry(dataIn):
    do = True
    total = 0
    matches = re.finditer(rf'(do\(\)|don\'t\(\))', dataIn)
        
    for match in matches:
        if do == True:
            total += calculations(dataIn)
        action = match.group(1)
        if action == 'do()':
            print('Currently calculating')
            do = True
        elif action == 'don\'t()':
            print('Not calculating')
            do = False

    return total

    


def calculations(data):
        result = 0
        matches2 = re.findall(rf'mul\((\d+),\s*(\d+)\)', data)
        for match in matches2:
            x = int(match[0])
            y = int(match[1])
            print('Multiplying')

            result += (x * y)

        return result



text = readData('input.txt')
print(thereIsNoTry(text))
