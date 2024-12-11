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
        do = True
        result = 0
        matches2 = re.findall(r"(?:mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data)
        for match in matches2:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            else:
                if do:
                    x = int(str(match[0]))
                    y = int(str(match[1]))
                    prod = x * y

                    result += prod

        return result



text = readData('input.txt')
print(calculations(text))
