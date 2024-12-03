from functools import reduce

def read_columns(file):
    col1, col2 = [], []
    with open(file, 'r') as f:
        for line in f:
            values = line.split('\t')
            if len(values) >= 2:
                col1.append(int(values[0]))
                col2.append(int(values[1]))
    return col1, col2

def getList1(pair):
    key, value = pair
    return key

def getList2(pair):
    key, value = pair
    return value


def sort(listIn):
    for i in range(len(listIn)):
        if (listIn[i] > listIn[i + 1]):
            listIn[i], listIn[i + 1] = listIn[i + 1], listIn[i]

def subtraction(lis1, lis2):
    total = 0
    for i in range(len(list1)):
        if(lis1[i] < lis2[i]):
            total += (lis2[i] - lis1[i])
        elif(lis1[i] > lis2[i]):
            total += (lis1[i] - lis2[i])
    return total

file = 'ex.txt'
dict1 = read_columns(file)
list1 = getList1(dict1)
list2 = getList2(dict1)
print(list1)


sort(list1)
sort(list2)
runningTotal = subtraction(list1, list2)


print(runningTotal)