import numpy as np

def countSafe(report):
    if len(report) <= 1:
        return 1
    diffs = np.diff(report)
    if(np.all(diffs >= 1) and np.all(diffs <= 3)):
        return 1
    if(np.all(diffs <= -1) and np.all(diffs >= -3)):
        return 1
    else:
        return 0

def countSafeWithRemoval(report):
    noRemovalNeeded = countSafe(report)
    if noRemovalNeeded == 0:
        for level in range(len(report)):
            if countSafe(np.delete(report, [level])):
                return 1
        return 0
    return noRemovalNeeded    

def howManySafe(reports):
    return sum(countSafe(r) for r in reports)

def problemDampener(reports):
    return np.sum([countSafeWithRemoval(r) for r in reports])


def readData(file):
    with open (file, 'r') as f:
        lines = f.readlines()
    reports = list()
    for line in lines:
        current = np.fromstring(line, dtype=int, sep=' ')
        reports.append(current)
    return np.array(reports, dtype=object)


reports = readData('reports.txt')
print(howManySafe(reports))
print(problemDampener(reports))
