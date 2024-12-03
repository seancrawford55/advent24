import math
def read_columns(file):
    col1, col2 = [], []
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        values = line.split()   
        col1.append(int(values[0]))
        col2.append(int(values[1]))
    return col1, col2


def subtraction(lis1, lis2):
    lis1.sort()
    lis2.sort()
    total = 0
    for i in range(len(list1)):
        total += (math.fabs(lis1[i] - lis2[i]))
    return total


list1, list2 = read_columns('ex.txt')

runningTotal = subtraction(list1, list2)


print(runningTotal)